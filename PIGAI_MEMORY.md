# Pigai 提分记忆（仅保留有效策略）

> 作文号 `3431395`。当前检查点 **95.5**（Run 168）。改写前先读本文，只采用下列已验证能提分或能避免掉分的做法。

## 最终作文（95.5）

```text
The person I hold in the highest regard is my grandmother, whose character has left a profound and indelible impression on me. Marked by patience, perseverance and responsibility, she has always cared for our family with quiet devotion. Above all, I admire the patience and responsibility she displays in supporting our family whenever difficulties arise.

First, I vividly remember receiving a disappointing grade at school and wanting to give up. Instead of criticizing me, she spared no effort to encourage me and helped restore my confidence. Second, she taught me to view difficulties as stepping stones to progress. Third, I learned from her that perseverance matters most when life becomes difficult, and that strength is shown through patience and responsibility.

Finally, that lesson, rooted in her perseverance and responsibility, has deeply influenced how I address difficulties. Then, whenever I encounter setbacks, whether at school or in daily life, I follow her example, maintain my composure and face challenges with patience and perseverance. Therefore, I have become more resilient, responsible and considerate. Moreover, she is not only the person I respect most, but also someone I will look up to and a constant source of strength.
```

维度：词汇 97.45 / 句子 95.18 / 结构 92.62 / 内容相关 95.05。词数约 195（略超 180 仍计分）。

## 已验证能提分的写法

1. **过程性连接词（结构）**  
   `First,` `Second,` `Third,` `Finally,` `Then,` `Moreover,`  
   → 篇章连词 1→2，结构 92.2→92.7，评语会出现「过程性词汇很丰富」。

2. **关系从句 + 分词前置（句子）**  
   `is my grandmother, whose character has left ...`  
   `Marked by patience, perseverance and responsibility, she has always cared ...`  
   → 句子分可到 95.2–95.4。

3. **安全的复杂插入（句子/结构）**  
   `whether at school or in daily life`  
   `profound and indelible impression`  
   → 提句子/词汇且不伤相关度。

4. **必须保留的闪光短语与语义链（相关度）**  
   - `hold ... in the highest regard`  
   - `leave an indelible impression on ...`  
   - `patience, perseverance and responsibility`  
   - `displays in supporting our family whenever difficulties arise`  
   - `receiving a disappointing grade at school and wanting to give up`  
   - `spare no effort to ...` / `restore my confidence`  
   - `view difficulties as stepping stones to progress`  
   - `maintain my composure`  
   - `look up to` / `a constant source of strength`  
   - `not only ... but also ...`  
   - `Therefore, I have become more resilient, responsible and considerate.`  
   - 语义链：patience → perseverance → responsibility → 具体事件 → resilient/responsible/considerate  

5. **`become more resilient` 优于 `grown stronger`**（曾把 94.5 抬到 95.0）。

6. **人物可换**（grandmother / father）：只要短语模板与故事场不变，相关度可守住；人物本身不是瓶颈。

7. **长句为主**：平均句长 20–21、最短句 ≥12 词时句子分最高。

## 必须避开的掉分写法

| 写法 | 后果 |
|------|------|
| 换故事线 / 换人物职业（如 retired nurse） | 相关度崩到 ~58，总分 85 |
| 强行短句（4–10 词） | 句子分 93→86，总分 93 |
| 重复 `restore my confidence`（如 Having restored...） | 相关度 95→89 |
| `my patient grandmother` / `warm-hearted` / `empty words` | 疑似中式英语 |
| `Guided by her example` | 相关度大跌 |
| 四段短 topic sentence 结构 | 句子分崩到 84，总分 92 |
| 合并首段长句、去掉 `Marked by...` 独立句 | 句子分掉到 92 |
| 堆高级短语（exerted a profound influence...） | 词汇升、总分降 |
| 机械追诊断参考范围（词长、学术词占比等） | 实际维度可能反向变差 |

## 诊断指标（只作参考，勿当目标）

- 从句类型 / 不定式 / 补语从句 / 关系从句 解析器常为 0，**不要为它们改写**。  
- 篇章连词即使写了 However/Moreover 也可能仍显示 1；**First/Second/Third/Finally/Then 才能抬到 2**。  
- 字数可略超 180；目标区间 175–200 均见过 95+。

## 上限（本作文号）

健康改写的显示分只会落在 **95.0 / 95.5**。  
四维上限约：词汇 97.6、句子 95.4、结构 92.7、相关 95.5。  
**96 及以上在此题不可达**；用户已接受 95.5 为最终分。

## 基础设施

- `.env`：`PIGAI_ACCOUNT` / `PIGAI_PASSWORD` / `PIGAI_ESSAY_ID=3431395`  
- 提交：`python main.py`（Chrome 路径已在 `pigai_agent/browser.py` 写死）  
- 结果：`artifacts/latest_feedback.json`；最优稿 `artifacts/best_95_5_essay.txt`  
- 仅改文档不会触发 CI 提交；`essay.txt` 变更才会。

## 停止条件

**用户已接受 95.5。非用户明确要求，不要再改写或重交。**
