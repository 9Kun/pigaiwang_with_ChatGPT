# pigaiwang_with_ChatGPT

把 2023 年的单文件脚本重构为一个可持续维护的 **批改网 + OpenAI 作文迭代工具**。

核心流程：

```text
当前作文
  ↓
提交到批改网
  ↓
抓取分数 + 总评 + 排名 + 按句点评 + 提示/搭配/闪光表达
  ↓
把完整反馈交给 OpenAI 修改
  ↓
生成下一版作文
  ↓
再次评分
  ↓
达到 TARGET_SCORE 后停止
```

例如：

```text
Round 1: 90
  ↓ 读取全部批改意见并修改
Round 2: 91
  ↓ 再修改
Round 3: 95
  ↓
Target reached. Stop.
```

> 为避免意外连续提交，每轮真正点击“提交/评分”前默认需要在终端按一次 Enter。评分结果解析、保存、AI 修改以及达到目标分后停止均自动完成。

## 2026 版相比旧版的变化

- 不再把账号、密码、API Key 写死在代码里。
- 移除写死的 Clash `127.0.0.1:7890`。
- 移除已经过时的 `gpt-3.5-turbo-16k` 调用方式。
- 使用 Selenium 4 + Chrome Selenium Manager，无需手工配置 chromedriver。
- 登录和页面元素使用多组 fallback selector，降低批改网页面改版后完全失效的概率。
- 不再只抓一个总分，反馈会保存成结构化 JSON。
- 每轮作文、反馈 JSON、页面截图都会保存，方便调试和比较。
- 自动记录历史最高分版本，不会因为后续修改降分而丢失最佳作文。
- 达到目标分自动结束；同时支持最大轮数保护。

## 可以返回什么

`PigaiFeedback` 当前会尝试解析并保存：

- 总分 `score`
- 排名 `rank`
- 总人数 `total_students`
- 最高分 / 最低分
- 词汇 / 句子 / 篇章结构 / 内容相关（页面可解析时）
- 总体评语
- 字数
- 提交次数
- 按句点评
- 错误 / 疑似错误 / 学习提示
- 闪光表达
- 推荐表达 / 近义词等建议
- 当前结果页 URL
- 页面完整文本 `raw_text`（用于页面改版后的兜底调试）

每轮还会保存一张完整页面截图。

## 安装

建议 Python 3.11+。

```bash
pip install -r requirements.txt
```

首次运行 Selenium 会通过 Selenium Manager 自动寻找/管理 Chrome 驱动。电脑需要已安装 Chrome 或兼容 Chromium 浏览器。

## 配置

复制：

```bash
copy .env.example .env
```

Linux/macOS：

```bash
cp .env.example .env
```

编辑 `.env`：

```dotenv
PIGAI_ACCOUNT=你的账号
PIGAI_PASSWORD=你的密码
PIGAI_ESSAY_ID=3431395
OPENAI_API_KEY=你的_OpenAI_API_Key
OPENAI_MODEL=gpt-5.6
TARGET_SCORE=95
MAX_ROUNDS=8
HEADLESS=false
```

`.env` 已写入 `.gitignore`，不要提交真实账号、密码或 API Key。

## 第一版作文从哪里来

程序会优先读取批改网页编辑器里当前已有的作文。

如果编辑器为空，请在仓库根目录建立：

```text
essay.txt
```

把第一版作文放进去即可。

## 运行

```bash
python main.py
```

典型输出：

```text
[1/3] Logging in...
[2/3] Opening essay #3431395...
Title: The Most Respectable Person in My Mind
Target score: 95.0
Max rounds: 8

=== Round 1 ===
...
Press Enter to submit this round, or Ctrl+C to stop:
Score: 90.0
Overall comment: ...
Sentence feedback items: 12
Sending the complete grader feedback to the optimizer...

=== Round 2 ===
...
Score: 91.0
...

=== Round 3 ===
...
Score: 95.0
Target reached: 95.0 >= 95.0. Stopping.
```

## 每轮输出文件

运行后会生成：

```text
artifacts/
├─ round_01_essay.txt
├─ round_01_feedback.json
├─ round_01.png
├─ round_02_essay.txt
├─ round_02_feedback.json
├─ round_02.png
├─ ...
├─ best_essay.txt
└─ best_feedback.json
```

其中 `best_essay.txt` 永远保存历史最高分对应的作文。

## AI 修改策略

下一轮不会简单“重新写一篇”，而是把以下内容一起发送给模型：

1. 作文标题
2. 原始题目要求
3. 当前作文全文
4. 当前批改网完整结构化反馈
5. 自动识别到的最低/最高字数限制

Prompt 要求模型：

- 优先修复批改网明确标出的错误和疑似错误；
- 保留没有被标错的高质量表达；
- 同时针对词汇、句子、篇章结构、内容相关等薄弱维度优化；
- 不为了“高级”而堆砌不自然的生词；
- 严格遵守作文题目和字数限制。

## 页面改版怎么办

批改网属于第三方网站，HTML、登录流程或验证码机制都可能随时修改。因此本项目没有声称 selector 永远有效。

2026 版做了三层兜底：

1. 同一元素准备多组 CSS/XPath selector；
2. 每轮保存页面截图；
3. 反馈 JSON 中保留 `raw_text`。

如果出现：

```text
Could not parse the score
```

先查看 `artifacts/round_xx.png` 和 `round_xx_feedback.json`，再按当前页面结构更新 `pigai_agent/browser.py` 中对应 selector/parser 即可。

## 项目结构

```text
main.py
pigai_agent/
├─ __init__.py
├─ config.py      # 环境变量配置
├─ models.py      # 结构化批改结果
├─ browser.py     # Selenium 登录、提交、结果解析
├─ ai.py          # OpenAI 反馈驱动改写
└─ runner.py      # 多轮迭代控制
```

## 注意

请只在你有权使用的账号和作文任务上运行，并遵守批改网及所在学校/课程的相关规则。第三方网站如果出现验证码、登录保护或提交频率限制，应人工完成验证，不要尝试绕过安全机制。
