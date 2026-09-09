# Agent Instructions

When optimizing `essay.txt` for Pigai:

1. **Read `PIGAI_MEMORY.md` first.** It is the persistent experiment memory and contains the current best score, validated flash phrases, failed experiments, hidden dimension values, and the next hypotheses to test.
2. Preserve the best verified checkpoint unless a controlled experiment beats it.
3. Do not blindly add rare vocabulary. The current bottleneck is no longer vocabulary; optimize the weakest dimensions reported by the latest Pigai result.
4. Prefer one-main-variable experiments and always evaluate the real Pigai score before carrying a change forward.
5. Keep the assignment's 120–180 word limit; target 175–179 words.
6. Stop only when a real Pigai result reaches the requested target score.
