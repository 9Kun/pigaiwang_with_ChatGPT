# pigaiwang_with_ChatGPT

2026 版改为 **外部 ChatGPT 负责改作文，仓库只负责登录批改网、提交作文并抓取完整批改结果**。

## 工作流

```text
ChatGPT 给出作文文本
        ↓
写入 essay.txt
        ↓
python main.py
        ↓
登录批改网并提交
        ↓
返回分数 + 总评 + 排名 + 按句点评 + 错误/疑似错误 + 推荐表达
        ↓
把反馈交给 ChatGPT 继续修改
        ↓
覆盖 essay.txt 后再次运行
        ↓
达到目标分后停止
```

例如：

```text
Round 1: 90
  ↓ 根据完整批改意见修改
Round 2: 91
  ↓ 再修改
Round 3: 95
  ↓ 停止
```

仓库本身不再调用 OpenAI API，因此不需要 `OPENAI_API_KEY`、`OPENAI_MODEL`，也不依赖 `openai` Python 包。

## 安装

```bash
pip install -r requirements.txt
```

需要本机安装 Chrome / Chromium。Selenium 4 会自动处理驱动。

## 配置

复制 `.env.example` 为 `.env`：

```dotenv
PIGAI_ACCOUNT=你的账号
PIGAI_PASSWORD=你的密码
PIGAI_ESSAY_ID=作文号
HEADLESS=false
```

`.env` 已被 `.gitignore` 忽略。不要把真实账号和密码提交到公开仓库历史中。

## 提交一轮

把这一轮作文放入仓库根目录：

```text
essay.txt
```

然后运行：

```bash
python main.py
```

程序会自动：

1. 登录批改网；
2. 打开指定作文号；
3. 将 `essay.txt` 覆盖到作文编辑器；
4. 提交评分；
5. 抓取评分结果；
6. 保存完整结果。

输出文件：

```text
artifacts/latest_essay.txt
artifacts/latest_feedback.json
artifacts/latest_result.png
```

`latest_feedback.json` 会尽量包含：

- `score`：总分
- `rank` / `total_students`：排名与人数
- `highest_score` / `lowest_score`
- `dimensions`：词汇、句子、篇章结构、内容相关（页面可解析时）
- `overall_comment`：总评
- `word_count`
- `submission_count`
- `sentence_reviews`：按句点评
- `highlights`：闪光表达
- `suggestions`：推荐表达、近义词等
- `raw_text`：完整结果页文本，用于页面改版时兜底调试
- `page_url`

## 当前迭代方式

不再让脚本自行调用模型连续改写。推荐由 ChatGPT 每轮根据真实批改结果决定下一版内容，避免模型在没有看到真实评分变化时盲目修改。

也就是说：

```text
我修改 essay.txt → 执行一次提交 → 读取真实反馈 → 再修改 essay.txt
```

这样可以精确保留已经被批改网认可的闪光短语，只修复被标出的错误、疑似错误以及当前最低维度。
