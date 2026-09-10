from __future__ import annotations

import re
import time
from pathlib import Path
from typing import Iterable

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from .models import PigaiFeedback, SentenceReview


class PigaiClient:
    HOME = "https://www.pigai.org/"

    def __init__(self, *, account: str, password: str, headless: bool = False) -> None:
        options = webdriver.ChromeOptions()
        if headless:
            options.add_argument("--headless=new")
        options.add_argument("--disable-notifications")
        options.add_argument("--window-size=1440,1200")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        chrome_binary = Path(r"C:\Program Files\Google\Chrome\Application\chrome.exe")
        if chrome_binary.exists():
            options.binary_location = str(chrome_binary)
        self.driver = webdriver.Chrome(options=options)
        self.driver.set_page_load_timeout(45)
        self.wait = WebDriverWait(self.driver, 15)
        self.account = account
        self.password = password

    def __enter__(self) -> "PigaiClient":
        return self

    def __exit__(self, exc_type, exc, tb) -> None:
        self.close()

    def close(self) -> None:
        try:
            self.driver.quit()
        except Exception:
            pass

    def _first(self, candidates: Iterable[tuple[str, str]], *, clickable: bool = False) -> WebElement:
        last: Exception | None = None
        for by, selector in candidates:
            try:
                condition = EC.element_to_be_clickable((by, selector)) if clickable else EC.presence_of_element_located((by, selector))
                return WebDriverWait(self.driver, 3).until(condition)
            except Exception as exc:
                last = exc
        raise TimeoutException(f"None of the selectors matched: {list(candidates)}") from last

    @staticmethod
    def _clear_and_type(element: WebElement, text: str) -> None:
        element.clear()
        element.send_keys(text)

    def _save_debug(self, stem: str) -> None:
        try:
            debug_dir = Path("artifacts")
            debug_dir.mkdir(parents=True, exist_ok=True)
            self.driver.save_screenshot(str(debug_dir / f"{stem}.png"))
            (debug_dir / f"{stem}.html").write_text(self.driver.page_source, encoding="utf-8")
        except Exception:
            pass

    def _open_home_with_retry(self, attempts: int = 3) -> None:
        last: Exception | None = None
        for attempt in range(1, attempts + 1):
            try:
                self.driver.get(self.HOME)
                return
            except Exception as exc:
                last = exc
                self._save_debug(f"home_load_failure_{attempt}")
                try:
                    self.driver.execute_script("window.stop();")
                except Exception:
                    pass
                if attempt < attempts:
                    time.sleep(float(attempt * 2))
        assert last is not None
        raise last

    def login(self) -> None:
        self._open_home_with_retry()
        username = self._first([
            (By.ID, "username"),
            (By.NAME, "username"),
            (By.CSS_SELECTOR, "input[type='text'][name*='user']"),
            (By.CSS_SELECTOR, "input[placeholder*='账号']"),
            (By.CSS_SELECTOR, "input[placeholder*='手机']"),
        ])
        password = self._first([
            (By.ID, "password"),
            (By.NAME, "password"),
            (By.CSS_SELECTOR, "input[type='password']"),
        ])
        self._clear_and_type(username, self.account)
        self._clear_and_type(password, self.password)

        WebDriverWait(self.driver, 10).until(
            lambda d: d.execute_script(
                "return typeof login === 'function' && typeof encrypt === 'function' && typeof JSEncrypt !== 'undefined';"
            )
        )
        old_url = self.driver.current_url
        self.driver.execute_script("login();")
        WebDriverWait(self.driver, 15).until(
            lambda d: d.current_url != old_url or "密码错误" in d.title or "账户密码不正确" in d.page_source
        )
        time.sleep(1.0)
        self._save_debug("after_login")
        if "密码错误" in self.driver.title or "账户密码不正确" in self.driver.page_source:
            raise RuntimeError("Pigai rejected the configured account/password.")

    def open_assignment(self, essay_id: str) -> None:
        try:
            search = self._first([
                (By.CSS_SELECTOR, "input[name='rid']"),
                (By.CSS_SELECTOR, "input[name*='request']"),
                (By.CSS_SELECTOR, "input[placeholder*='作文号']"),
                (By.XPATH, "/html/body/div[4]/div[3]/form/div[2]/input[1]"),
            ])
        except Exception:
            self._save_debug("assignment_search_failure")
            raise
        self._clear_and_type(search, essay_id)
        submit = self._first([
            (By.XPATH, "//button[contains(.,'进入') or contains(.,'搜索') or contains(.,'查找')]"),
            (By.XPATH, "/html/body/div[4]/div[3]/form/div[3]/button"),
        ], clickable=True)
        submit.click()
        WebDriverWait(self.driver, 15).until(lambda d: essay_id in d.page_source or "作文" in d.title)
        time.sleep(1.0)

    def _essay_editor(self) -> WebElement:
        return self._first([
            (By.CSS_SELECTOR, "textarea"),
            (By.CSS_SELECTOR, "[contenteditable='true']"),
            (By.ID, "contents"),
            (By.NAME, "contents"),
        ])

    def submit_essay(self, essay_text: str) -> None:
        editor = self._essay_editor()
        if editor.tag_name.lower() == "textarea":
            self._clear_and_type(editor, essay_text)
        else:
            self.driver.execute_script(
                "arguments[0].innerHTML = ''; arguments[0].innerText = arguments[1]; arguments[0].dispatchEvent(new Event('input', {bubbles:true}));",
                editor,
                essay_text,
            )

        submit = self._first([
            (By.XPATH, "//button[contains(.,'提交') or contains(.,'保存')]"),
            (By.XPATH, "//input[@type='submit']"),
        ], clickable=True)
        old_url = self.driver.current_url
        submit.click()
        WebDriverWait(self.driver, 20).until(
            lambda d: d.current_url != old_url or "得分" in d.page_source or "分" in d.title
        )
        time.sleep(2.0)

    def parse_feedback(self) -> PigaiFeedback:
        html = self.driver.page_source
        text = BeautifulSoup(html, "html.parser").get_text("\n", strip=True)
        score = self._parse_score(text)
        rank, total_students = self._parse_rank(text)
        highest_score, lowest_score = self._parse_extremes(text)
        dimensions = self._parse_dimensions(text)
        reviews = self._parse_sentence_reviews(text)
        suggestions = [review.comment for review in reviews if review.category in {"推荐表达", "拓展辨析", "近义词表达学习"}]
        word_count = self._parse_word_count(text)
        submission_count = self._parse_submission_count(text)
        return PigaiFeedback(
            score=score,
            rank=rank,
            total_students=total_students,
            highest_score=highest_score,
            lowest_score=lowest_score,
            dimensions=dimensions,
            overall_comment=self._parse_overall_comment(text),
            word_count=word_count,
            submission_count=submission_count,
            sentence_reviews=reviews,
            highlights=[],
            suggestions=suggestions,
            page_url=self.driver.current_url,
            raw_text=text,
        )

    @staticmethod
    def _parse_score(text: str) -> float:
        patterns = [
            r"(?:得分|总分|评分)\s*[:：]?\s*(\d+(?:\.\d+)?)",
            r"\b(\d+(?:\.\d+)?)\s*分\b",
        ]
        candidates: list[float] = []
        for pattern in patterns:
            for match in re.finditer(pattern, text):
                value = float(match.group(1))
                if 0 <= value <= 100:
                    candidates.append(value)
        if not candidates:
            raise ValueError("Unable to parse Pigai score from result page.")
        return max(candidates)

    @staticmethod
    def _parse_rank(text: str) -> tuple[int | None, int | None]:
        patterns = [
            r"排名\s*[:：]?\s*(\d+)\s*/\s*(\d+)",
            r"第\s*(\d+)\s*名.*?(?:共|/|总)\s*(\d+)",
        ]
        for pattern in patterns:
            match = re.search(pattern, text, flags=re.S)
            if match:
                return int(match.group(1)), int(match.group(2))
        return None, None

    @staticmethod
    def _parse_extremes(text: str) -> tuple[float | None, float | None]:
        high = re.search(r"(?:最高|最高分)\s*[:：]?\s*(\d+(?:\.\d+)?)", text)
        low = re.search(r"(?:最低|最低分)\s*[:：]?\s*(\d+(?:\.\d+)?)", text)
        return (float(high.group(1)) if high else None, float(low.group(1)) if low else None)

    @staticmethod
    def _parse_dimensions(text: str) -> dict[str, float | None]:
        labels = {
            "vocabulary": ["词汇"],
            "sentence": ["句子", "句法"],
            "structure": ["篇章结构", "结构"],
            "relevance": ["内容相关", "相关度", "切题"],
        }
        result: dict[str, float | None] = {key: None for key in labels}
        for key, variants in labels.items():
            for label in variants:
                match = re.search(rf"{label}\s*[:：]?\s*(\d+(?:\.\d+)?)", text)
                if match:
                    result[key] = float(match.group(1))
                    break
        return result

    @staticmethod
    def _parse_overall_comment(text: str) -> str:
        marker = "类型\n维度\n测量值\n参考范围"
        if marker in text:
            return text.split(marker, 1)[0][-1200:]
        return text[:1200]

    @staticmethod
    def _parse_word_count(text: str) -> int | None:
        match = re.search(r"字数\s*[:：]?\s*(\d+)", text)
        return int(match.group(1)) if match else None

    @staticmethod
    def _parse_submission_count(text: str) -> int | None:
        for pattern in [r"提交次数\s*[:：]?\s*(\d+)", r"提交\s*(\d+)\s*次"]:
            match = re.search(pattern, text)
            if match:
                return int(match.group(1))
        return None

    @staticmethod
    def _parse_sentence_reviews(text: str) -> list[SentenceReview]:
        categories = ["拓展辨析", "学习提示", "推荐表达", "近义词表达学习", "语法", "搭配"]
        reviews: list[SentenceReview] = []
        for category in categories:
            for match in re.finditer(rf"\[{category}\](.+?)(?=\[(?:{'|'.join(categories)})\]|$)", text, flags=re.S):
                comment = match.group(1).strip()
                if not comment:
                    continue
                reviews.append(
                    SentenceReview(
                        sentence="",
                        category=category,
                        level="info",
                        target="",
                        comment=comment,
                    )
                )
        return reviews
