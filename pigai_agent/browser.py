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
        self.driver = webdriver.Chrome(options=options)
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

    def login(self) -> None:
        self.driver.get(self.HOME)
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

        # Use Pigai's own current login() implementation. It RSA-encrypts the
        # password into #password_encrypt and submits the form through jQuery,
        # including any submit handlers the site may attach.
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
            (By.CSS_SELECTOR, "form button[type='submit']"),
        ], clickable=True)
        self.driver.execute_script("arguments[0].click();", submit)
        time.sleep(1.5)

    def assignment_info(self) -> tuple[str, str]:
        title = ""
        requirements = ""
        try:
            node = self._first([
                (By.ID, "request_y"),
                (By.CSS_SELECTOR, "[id*='request']"),
            ])
            requirements = BeautifulSoup(node.get_attribute("innerHTML") or node.text, "html.parser").get_text(" ", strip=True)
        except Exception:
            pass

        soup = BeautifulSoup(self.driver.page_source, "html.parser")
        for selector in ["h1", "h2", ".title", "#title"]:
            node = soup.select_one(selector)
            if node and node.get_text(strip=True):
                title = node.get_text(" ", strip=True)
                break
        if not title:
            title = "English Essay"
        return title, requirements

    def current_essay(self) -> str:
        editor = self._first([
            (By.ID, "contents"),
            (By.NAME, "contents"),
            (By.CSS_SELECTOR, "textarea"),
            (By.CSS_SELECTOR, "[contenteditable='true']"),
        ])
        value = editor.get_attribute("value")
        return (value if value is not None else editor.text).strip()

    def submit_essay(self, essay: str) -> None:
        editor = self._first([
            (By.ID, "contents"),
            (By.NAME, "contents"),
            (By.CSS_SELECTOR, "textarea"),
            (By.CSS_SELECTOR, "[contenteditable='true']"),
        ])
        if editor.get_attribute("contenteditable") == "true":
            self.driver.execute_script("arguments[0].innerText = arguments[1];", editor, essay)
        else:
            self._clear_and_type(editor, essay)

        button = self._first([
            (By.ID, "dafen"),
            (By.XPATH, "//button[contains(.,'提交') or contains(.,'批改') or contains(.,'评分')]"),
            (By.CSS_SELECTOR, "button[type='submit']"),
        ], clickable=True)
        self.driver.execute_script("arguments[0].click();", button)
        time.sleep(4)

    @staticmethod
    def _num(pattern: str, text: str) -> float | None:
        match = re.search(pattern, text, re.I | re.S)
        return float(match.group(1)) if match else None

    def parse_feedback(self) -> PigaiFeedback:
        html = self.driver.page_source
        soup = BeautifulSoup(html, "html.parser")
        text = soup.get_text("\n", strip=True)
        feedback = PigaiFeedback(page_url=self.driver.current_url, raw_text=text)

        score_patterns = [
            r"作文评分\s*([0-9]+(?:\.[0-9]+)?)",
            r"得分(?:为|[:：])?\s*([0-9]+(?:\.[0-9]+)?)",
            r"score\s*[:：]?\s*([0-9]+(?:\.[0-9]+)?)",
        ]
        for pattern in score_patterns:
            feedback.score = self._num(pattern, text)
            if feedback.score is not None:
                break
        if feedback.score is None:
            for selector in [".score", "#score", "[class*='score']", "[id*='score']"]:
                node = soup.select_one(selector)
                if node:
                    m = re.search(r"\b([0-9]{1,3}(?:\.[0-9]+)?)\b", node.get_text(" ", strip=True))
                    if m:
                        feedback.score = float(m.group(1))
                        break

        m = re.search(r"排名\s*[:：]?\s*第?\s*(\d+)\s*\(共\s*(\d+)\s*\)", text)
        if m:
            feedback.rank, feedback.total_students = int(m.group(1)), int(m.group(2))
        feedback.highest_score = self._num(r"最高分\s*[:：]?\s*([0-9]+(?:\.[0-9]+)?)", text)
        feedback.lowest_score = self._num(r"最低分\s*[:：]?\s*([0-9]+(?:\.[0-9]+)?)", text)
        wc = re.search(r"字数\s*[:：]?\s*(\d+)", text)
        if wc:
            feedback.word_count = int(wc.group(1))
        sc = re.search(r"提交次数\s*[:：]?\s*(\d+)", text)
        if sc:
            feedback.submission_count = int(sc.group(1))

        comment = re.search(r"评语\s*[:：]\s*(.+?)(?:按句点评|第\s*1\s*段|$)", text, re.S)
        if comment:
            feedback.overall_comment = re.sub(r"\s+", " ", comment.group(1)).strip()

        for label, key in [("词汇", "vocabulary"), ("句子", "sentence"), ("篇章结构", "structure"), ("内容相关", "relevance")]:
            value = self._num(rf"{label}\s*[:：]?\s*([0-9]+(?:\.[0-9]+)?)", text)
            feedback.dimensions[key] = value

        review_nodes = soup.select("[class*='comment'], [class*='review'], [class*='sentence'], [class*='point']")
        seen: set[str] = set()
        for node in review_nodes:
            chunk = re.sub(r"\s+", " ", node.get_text(" ", strip=True))
            if len(chunk) < 12 or chunk in seen:
                continue
            if any(mark in chunk for mark in ["错误", "警示", "提示", "推荐表达", "搭配", "近义词", "闪光"]):
                seen.add(chunk)
                level = "error" if "错误" in chunk else "warning" if "警示" in chunk else "info"
                feedback.sentence_reviews.append(SentenceReview(comment=chunk, level=level))
                if "闪光" in chunk:
                    feedback.highlights.append(chunk)
                if "推荐" in chunk or "近义" in chunk:
                    feedback.suggestions.append(chunk)

        return feedback

    def screenshot(self, path: str | Path) -> None:
        Path(path).parent.mkdir(parents=True, exist_ok=True)
        self.driver.save_screenshot(str(path))
