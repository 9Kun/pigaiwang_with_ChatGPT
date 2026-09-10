# Pigai 提分记忆（仅保留有效策略）

> 作文号 `3431395`。当前最高检查点 **96.0（Run 151）**，排名 **1/71**。改写前先读本文，避免被旧的 95/95.5 结论带回去。

## 最终作文（96.0）

```text
The person I hold in the highest regard is my grandmother, whose character has left a profound and indelible impression on me. Marked by patience, perseverance and responsibility, she has always cared for our family with quiet devotion. Above all, I admire the patience and responsibility she displays in supporting our family whenever difficulties arise.

First, I vividly remember receiving a disappointing grade at school and wanting to give up. Nevertheless, instead of criticizing me, she spared no effort to encourage me and helped restore my confidence. Second, she taught me to view difficulties as stepping stones to progress. Third, I learned from her that perseverance matters most when life becomes difficult, and that strength is shown through patience and responsibility.

Finally, that lesson, rooted in her perseverance and responsibility, has deeply influenced how I address difficulties. Thereafter, whenever I encounter setbacks, whether at school or in daily life, I follow her example, maintain my composure and face challenges with patience and perseverance. Therefore, I have become more resilient, responsible and considerate. For these reasons, she is not only the person I respect most, but also someone I will look up to and a constant source of strength.
```

真实批改结果：**96.0**；词汇 **97.6547** / 句子 **95.4900** / 结构 **92.8360** / 内容相关 **95.0498**；平台统计字数约 **198**。

## 这次从 95.5 突破到 96.0 的关键

1. 以 Run 148 的高分骨架为母版：`Thereafter` + `Therefore` + `For these reasons`，并保留 `First / Second / Third / Finally` 的过程性组织。
2. 唯一关键替换：
   - `However, instead of criticizing me, ...`
   - → **`Nevertheless, instead of criticizing me, ...`**
3. 这次替换后四维同时达到目前最佳综合状态：词汇 97.65、句子 95.49、结构 92.84，最终显示分由 95.5 跨到 96.0。
4. **严格压缩到 180 词没有突破**：Run 150 仍为 95.5，虽然 relevance 升到约 95.36，但 sentence / structure 明显下降。因此不要为了机械满足 180 词而破坏当前骨架。

## 必须保留的高收益表达与结构

- `hold ... in the highest regard`
- `profound and indelible impression`
- `Marked by patience, perseverance and responsibility`
- `quiet devotion`
- `receiving a disappointing grade at school and wanting to give up`
- `spared no effort to encourage me`
- `restore my confidence`
- `view difficulties as stepping stones to progress`
- `perseverance matters most when life becomes difficult`
- `that strength is shown through patience and responsibility`
- `that lesson, rooted in her perseverance and responsibility`
- `whether at school or in daily life`
- `maintain my composure`
- `become more resilient, responsible and considerate`
- `not only ... but also ...`
- `look up to`
- `a constant source of strength`
- 连接词顺序：`First` → `Nevertheless` → `Second` → `Third` → `Finally` → `Thereafter` → `Therefore` → `For these reasons`

## 已验证的掉分方向

- `Consequently` 替代 `Therefore`：仍 95.5，结构下降。
- `Since then` 替代 `Thereafter`：仍 95.5，综合不如当前版。
- 结尾强行复述 `most respectable person` / `admire most`：没有抬高总分或相关度。
- 强行压到 180 词：总分仍 95.5，sentence / structure 下降。
- 换故事线、换职业、四段短 topic sentence、强行堆高级词、`Guided by her example` 等旧路线均已验证会掉分。

## 基础设施

- 提交源：`essay.txt`
- Workflow：`.github/workflows/pigai-run.yml`
- 真实结果：`LATEST_PIGAI_FEEDBACK.json`
- 只有 `essay.txt` 变更会触发自动提交；更新本文档不会再次提交作文。

## 当前停止条件

**目标 96.0 已于 Run 151 实测达到。默认锁定当前 `essay.txt`，不要再自动改写或重交；只有用户明确提出更高目标时才继续。**
