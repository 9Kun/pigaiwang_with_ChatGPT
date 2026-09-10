# Pigai High-Score Memory

> Persistent experiment memory for `essay.txt`. Read this file before editing. Trust real Pigai A/B results over intuition. Preserve the best verified checkpoint, change one primary linguistic variable per round, and never promote a lower-scoring variant merely because one diagnostic dimension improved.

## Current objective

- Target: **verified Pigai score >= 95.0**.
- Do not claim success until a real submission reports `score >= 95.0`.
- Current best verified headline score: **94.5**, rank 1.
- Best role/topic: **grandmother**, with direct personal interaction and long-term influence.

## Strongest current checkpoint — Run 128

Essay commit: `efe073e1b5bc6ffb64db78d55896fb4a1181d0e1`.
Pigai score: **94.5**; Pigai word count: **180**; rank **1/65**.
Hidden dimensions: vocabulary **97.1568**, sentence **93.3505**, structure **91.0002**, relevance **91.1311**.
This is the first verified 94.5 checkpoint and remains the safest active baseline.

### Run 128 text

```text
The person I hold in the highest regard is my grandmother. Her character, marked by patience, perseverance and responsibility, has left an indelible impression on me. Above all, I admire the patience and responsibility with which she supports our family whenever difficulties arise.

To illustrate this, I vividly remember receiving a disappointing grade at school and wanting to give up. Instead of criticizing me, she spared no effort to encourage me and helped restore my confidence. She taught me to view difficulties as stepping stones to progress. More significantly, I learned from her that perseverance matters most when life becomes difficult, and that strength is shown through patience and responsibility.

Beyond that experience, her example of perseverance and responsibility has deeply influenced the way I address difficulties. Whenever I encounter setbacks, I follow her example, maintain my composure and face challenges with patience and perseverance. Therefore, I have grown stronger, more responsible and considerate. For these reasons, she is not only the person I respect most, but also someone I will look up to and a constant source of strength.
```

## Equal 94.5 variant — Run 131

Essay commit: `a27dbc997a3d8bcfe2bac725112dbdafba31023f`.
Changed only the first-paragraph phrase from `the patience and responsibility with which she supports...` to `the patience and responsibility she displays in supporting...`.
Pigai score: **94.5**; vocabulary **97.3361**, sentence **93.3505**, structure **91.0339**, relevance **91.0981**.
Interpretation: naturalized wording is essentially neutral at headline score; slightly stronger vocabulary/structure and negligibly weaker relevance. It may be used as an equal checkpoint, but Run 128 remains the canonical baseline.

## Preserve by default

- `hold ... in the highest regard`
- `leave an indelible impression on ...`
- `spare no effort to ...`
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
- evidence wording `receiving a disappointing grade at school and wanting to give up`
- semantic chain: **patience -> perseverance -> responsibility -> changed behavior / stronger self**.

## Important recent experiments

- Run 119: third-paragraph `patience and responsibility` instead of `patience and perseverance`; **92.5**. Relevance collapsed to **72.2948**. Reject.
- Run 121: `Beyond this experience` instead of `Beyond that experience`; **94.0**, neutral. No gain.
- Run 122: conclusion `Taken together, these qualities ...`; **94.0**. Structure fell. Reject.
- Run 123: four-paragraph layout; **94.0**. Structure fell. Keep 3 paragraphs.
- Run 124: split concrete exam evidence into two short sentences; **93.0**. Structure rose to **91.1025**, but sentence score collapsed to **89.3552**. Reject short-sentence optimization.
- Run 125: `a disappointing exam result that nearly made me give up`; **94.0**. Structure **90.7620**, relevance **91.0152**. Reject versus Run 128.
- Run 126: `a disappointing exam result that nearly made me lose confidence`; **94.0**. Relevance fell to **90.2150**. Reject.
- Run 127: `Her example has made me resilient, responsible and considerate.`; **94.0**. Structure/relevance both fell. Reject.
- **Run 128**: `receiving a disappointing grade at school and wanting to give up`; **94.5**. Promote to active baseline.
- Run 129: `a disappointing grade at school that almost made me give up`; **94.0**. Sentence rose slightly but vocabulary/structure fell. Reject.
- Run 130: `has exerted a profound influence on me far beyond that experience`; **93.5**. Vocabulary rose to **97.5569** and Pigai flagged a flash phrase, but sentence fell to **90.6964** and relevance to **90.3548**. Reject; do not chase advanced phrases.
- **Run 131**: `she displays in supporting...`; **94.5**. Equal checkpoint, not a clear promotion over Run 128.

## Diagnostic priority

On the 94.5 line:
1. vocabulary ~97.2–97.3 — already excellent; do not chase rare vocabulary.
2. sentence ~93.35 — strong; small naturalness gains may matter.
3. relevance ~91.1 — needs improvement, but keyword repetition can backfire.
4. structure ~91.0 — weakest; prioritize genuine logical linkage between evidence and long-term influence.

Do not optimize diagnostic reference ranges mechanically. Earlier forced short sentences, adjective-ratio changes, and advanced phrase stacking all lowered the headline score.

## Infrastructure

- `.github/workflows/pigai-run.yml` triggers grading only when `essay.txt` changes (or manual dispatch).
- Successful grading creates artifacts containing `latest_feedback.json`, `latest_result.html`, `latest_result.png`, and `latest_essay.txt`.
- `LATEST_PIGAI_FEEDBACK.json` is convenient but not authoritative if post-grading persistence fails; inspect the artifact in that case.
- Documentation-only changes do not trigger a Pigai submission.

## Iteration rule

Start each new experiment from Run 128, or from Run 131 only when intentionally preserving its first-paragraph naturalization. Promote a new checkpoint only if it scores above **94.5**, or if it ties **94.5** with a clearly stronger balanced hidden profile without a meaningful relevance/structure loss.

Only one primary linguistic variable per submission. If a variant scores below the active checkpoint, revert before the next experiment.

## Stop condition

**Stop only after a real Pigai result reports score >= 95.0.**
