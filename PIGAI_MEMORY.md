# Pigai 提分记忆（仅保留有效策略）

> 作文号 `3431395`。当前真实最高检查点 **96.5**。用户当前目标：**98.0**。继续实验时必须从已验证的 96.5 checkpoint 出发；低于 96.5 的实验不得覆盖最高母版。

## 当前高相关 96.5 checkpoint

```text
The person I hold in the highest regard is my grandmother, whose character has left a profound and indelible impression on me. Marked by patience, perseverance and responsibility, she has always cared for our family with quiet devotion. Specifically, I admire the patience and responsibility she displays in supporting our family whenever difficulties arise.

To illustrate this, I vividly remember receiving a disappointing grade at school and wanting to give up. Nevertheless, instead of criticizing me, she spared no effort to encourage me and restore my confidence. Furthermore, she taught me to view difficulties as stepping stones to progress. More significantly, I learned a lasting lesson from her: perseverance matters most when life becomes difficult, and true strength is shown through patience and responsibility.

Finally, that lesson, rooted in her perseverance and responsibility, has profoundly shaped how I address difficulties. Subsequently, whenever I encounter setbacks, particularly in my studies, I follow her example, maintain my composure and face challenges with patience and perseverance. Therefore, I have gradually become more resilient, responsible and considerate. For these reasons, she is not only the person I respect most, but also someone I will look up to and a constant source of strength.
```

已验证结果：**96.5**；词汇 **98.1900** / 句子 **96.0479** / 结构 **93.1209** / 内容相关 **95.2235**；平台统计约 197 词。

## 另一条 96.5 高词汇 checkpoint

把 `quiet devotion` 改为 `selfless devotion`，同时保留 `a lasting lesson from her`，也得到 **96.5**：词汇约 **98.2787** / 句子 **96.0479** / 结构 **93.1515** / 内容相关 **95.0865**。它适合做词汇侧实验，但综合相关性略低于上面的高相关 checkpoint。

## 96.5 阶段已验证的规律

- `Nevertheless` 必须保留；它曾把 95.5 推到 96.0。
- `Subsequently` 比 `Thereafter` 的结构隐藏分略好。
- `Therefore` 优于 `Accordingly` / `Consequently`。
- `a lasting lesson from her` 是 96.5 关键结构之一，优于泛化的 `I learned this from her`。
- `selfless devotion` 能抬词汇，但必须与高相关 lesson 结构组合，不能单独据一次低相关实验下结论。
- 将最后一句拆成两句能抬 sentence/structure（曾到约 96.38 / 93.35），但 relevance 会明显下降，因此不能作为当前主母版。
- `confront adversity`、`examination result`、额外 wh-clause、`Specifically, what I admire most...` 等后续组合均未超过 96.5。
- 严格压到 180 词会损失 sentence/structure；当前目标不是机械满足诊断区间，而是实际批改分。

## 必须保留的高收益表达

- `hold ... in the highest regard`
- `profound and indelible impression`
- `Marked by patience, perseverance and responsibility`
- `quiet devotion` / 可控测试 `selfless devotion`
- `Specifically, I admire ...`
- `To illustrate this`
- `vividly remember receiving a disappointing grade at school and wanting to give up`
- `Nevertheless, instead of criticizing me`
- `spared no effort to encourage me and restore my confidence`
- `view difficulties as stepping stones to progress`
- `More significantly`
- `a lasting lesson from her`
- `perseverance matters most when life becomes difficult`
- `true strength is shown through patience and responsibility`
- `that lesson, rooted in her perseverance and responsibility`
- `profoundly shaped how I address difficulties`
- `Subsequently`
- `particularly in my studies`
- `maintain my composure`
- `Therefore, I have gradually become more resilient, responsible and considerate`
- `not only ... but also ...`
- `look up to`
- `a constant source of strength`

## 基础设施与规则

- 提交源：`essay.txt`
- Workflow：`.github/workflows/pigai-run.yml`
- 真实结果：`LATEST_PIGAI_FEEDBACK.json`
- 只有修改 `essay.txt` 才触发批改；更新本文档不会提交作文。
- 每轮只做一个可归因变量；记录实际分和四维。
- 不重复已经明确失败的实验；不把低分版本当母版。

## 当前停止条件

**只有真实批改网分数达到或超过 98.0 才停止。当前最高 96.5，继续优化。**
