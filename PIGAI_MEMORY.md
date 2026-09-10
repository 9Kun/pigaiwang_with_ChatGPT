# Pigai High-Score Memory

> Persistent experiment memory for `essay.txt`. Read this file before editing. Trust real Pigai A/B results over intuition. Preserve the best verified checkpoint and change one main variable per round. Never promote a lower-scoring variant merely because one diagnostic dimension improved.

## Current objective

- Target: **verified Pigai score >= 95.0**.
- Do not claim success until a real submission reports `score >= 95.0`.
- Current best verified headline score: **94.0**, rank 1.
- Best role/topic: **grandmother**, direct personal interaction and long-term influence.

## Strongest current checkpoint — Run 118

Source essay commit: `88c328e6629c9f0496883bd9ae63454f0d070ba3`.
Result commit: `4389516e07d2f57efdebf509e8c2f76c0df43b18`.
Pigai score: **94.0**; Pigai word count: **180**.
Hidden dimensions: vocabulary **96.7183**, sentence **93.4581**, structure **90.5777**, relevance **91.2899**.
This remains the best balanced checkpoint after Runs 119–127.

### Run 118 text

```text
The person I hold in the highest regard is my grandmother. Her character, marked by patience, perseverance and responsibility, has left an indelible impression on me. Above all, I admire the patience and responsibility with which she supports our family whenever difficulties arise.

To illustrate this, I vividly remember when I performed poorly at school and wanted to give up. Instead of criticizing me, she spared no effort to encourage me and helped restore my confidence. She taught me to view difficulties as stepping stones to progress. More significantly, I learned from her that perseverance matters most when life becomes difficult, and that strength is shown through patience and responsibility.

Beyond that experience, her example of perseverance and responsibility has deeply influenced the way I address difficulties. Whenever I encounter setbacks, I follow her example, maintain my composure and face challenges with patience and perseverance. Therefore, I have grown stronger, more responsible and considerate. For these reasons, she is not only the person I respect most, but also someone I will look up to and a constant source of strength.
```

## Preserve by default

- `hold ... in the highest regard`
- `leave an indelible impression on ...`
- `spare no effort to ...` — Pigai-recognized strong sentence pattern.
- `view difficulties as stepping stones to progress`
- `restore my confidence`
- `maintain my composure`
- `look up to`
- `a constant source of strength`
- `not only ... but also ...`
- `Above all,`
- `To illustrate this,`
- `More significantly,`
- `Therefore,`
- semantic chain: **patience -> perseverance -> responsibility -> changed behavior / stronger self**.

## Important recent experiments

- Run 119: changed third-paragraph `patience and perseverance` to `patience and responsibility`; **92.5**. Relevance collapsed to **72.2948**. Reject.
- Run 120: old Run-54 line with `Through that experience`; **93.0**, 181 Pigai words. Reject.
- Run 121: `Beyond this experience` instead of `Beyond that experience`; **94.0**, hidden dimensions effectively identical to Run 118. Neutral.
- Run 122: conclusion changed to `Taken together, these qualities ...`; **94.0**. Vocabulary/sentence rose, structure fell to **89.6855**. Reject as baseline.
- Run 123: conclusion isolated as paragraph 4; **94.0**. Structure fell to **90.2868**. Keep 3 paragraphs.
- Run 124: concrete exam evidence split into two short sentences; **93.0**. Structure rose to **91.1025**, but sentence score collapsed to **89.3552**. Reject.
- Run 125: recombined as `a disappointing exam result that nearly made me give up`; **94.0**. Structure **90.7620**, relevance **91.0152**. Weaker balance than Run 118.
- Run 126: `a disappointing exam result that nearly made me lose confidence`; **94.0**. Structure **90.8523**, relevance **90.2150**. Reject.
- **Run 127 / `d266338f925d5cce59175e26678bfaf19c0788d9`**: restored Run-118 wording and changed only `Therefore, I have grown stronger, more responsible and considerate.` to `Her example has made me resilient, responsible and considerate.`; **94.0**, **180 words**, rank **1/65**. Hidden dimensions: vocabulary **96.9980**, sentence **93.3510**, structure **89.3674**, relevance **90.7761**. Vocabulary rose slightly, but sentence, structure, and relevance all fell versus Run 118. **Reject; do not promote.** The Pigai submission and artifact generation succeeded, but the workflow's persistence step failed afterward, so use the Run-127 artifact as the authoritative result for this run.

## Diagnostic priority

On Run 118 the dimensions are roughly:
1. vocabulary 96.72 — already excellent; do not chase obscure words.
2. sentence 93.46 — strong, still capable of small gains.
3. relevance 91.29 — needs improvement but is sensitive to mechanical repetition.
4. structure 90.58 — weakest; improve genuine logical cohesion rather than merely adding connectors.

Runs 124–127 reinforce that seemingly more explicit phrasing can improve one local metric while damaging the balanced profile. Do not replace `Therefore, I have grown stronger, more responsible and considerate.` with a direct `Her example has made me ...` construction.

## Infrastructure

- `.github/workflows/pigai-run.yml` triggers only when `essay.txt` changes (or manual dispatch).
- Successful grading creates an artifact containing `latest_feedback.json`, `latest_result.html`, `latest_result.png`, and `latest_essay.txt`.
- `LATEST_PIGAI_FEEDBACK.json` is convenient but is not authoritative if the post-grading persistence step fails; in that case inspect the artifact directly.
- Documentation-only changes do not trigger a Pigai submission.

## Iteration rule

Start each new experiment from Run 118 unless a newer variant achieves either:
- headline score > 94.0, or
- the same 94.0 with a clearly stronger balanced hidden profile and no loss in key relevance/structure signals.

Only one primary linguistic variable per submission. If a variant scores below the active checkpoint, revert rather than stacking additional edits on it.

## Stop condition

**Stop only after a real Pigai result reports score >= 95.0.**
