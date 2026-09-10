# Pigai High-Score Memory

> Persistent experiment memory for `essay.txt`. Read this file before editing. Trust real Pigai A/B results over intuition. Preserve the best verified checkpoint, change one primary linguistic variable per round, and never promote a lower-scoring variant merely because one diagnostic dimension improved.

## Current objective

- Target: **verified Pigai score >= 95.0**.
- Do not claim success until a real submission reports `score >= 95.0`.
- Current best verified headline score: **94.5**, rank 1.
- Best role/topic: **grandmother**, with direct personal interaction and long-term influence.

## Strongest balanced checkpoint — Run 132

Essay commit: `5ca3412f5e4057ddcb45e520ac2d67a74e084437`.
Pigai score: **94.5**; Pigai word count: **178**; rank **1/65**.
Hidden dimensions: vocabulary **97.3197**, sentence **93.4484**, structure **91.0732**, relevance **95.7044**.
This is the strongest balanced checkpoint so far: compared with Run 128, it keeps the same 94.5 headline score while improving vocabulary, sentence, structure, and especially relevance.

### Run 132 text

```text
The person I hold in the highest regard is my grandmother. Her character, marked by patience, perseverance and responsibility, has left an indelible impression on me. Above all, I admire the patience and responsibility she displays in supporting our family whenever difficulties arise.

To illustrate this, I vividly remember receiving a disappointing grade at school and wanting to give up. Instead of criticizing me, she spared no effort to encourage me and helped restore my confidence. She taught me to view difficulties as stepping stones to progress. More significantly, I learned from her that perseverance matters most when life becomes difficult, and that strength is shown through patience and responsibility.

That lesson, rooted in her perseverance and responsibility, has deeply influenced how I address difficulties. Whenever I encounter setbacks, I follow her example, maintain my composure and face challenges with patience and perseverance. Therefore, I have grown stronger, more responsible and considerate. For these reasons, she is not only the person I respect most, but also someone I will look up to and a constant source of strength.
```

## Earlier 94.5 checkpoints

- **Run 128 / `efe073e1b5bc6ffb64db78d55896fb4a1181d0e1`**: first verified 94.5, 180 words. Dimensions: vocabulary **97.1568**, sentence **93.3505**, structure **91.0002**, relevance **91.1311**. Key gain came from `receiving a disappointing grade at school and wanting to give up`.
- **Run 131 / `a27dbc997a3d8bcfe2bac725112dbdafba31023f`**: first-paragraph naturalization `she displays in supporting...`; **94.5**. Dimensions: vocabulary **97.3361**, sentence **93.3505**, structure **91.0339**, relevance **91.0981**.
- **Run 132**: changed the third-paragraph bridge to `That lesson, rooted in her perseverance and responsibility, has deeply influenced how I address difficulties.`; **94.5**, relevance jumped to **95.7044**. Promote as strongest balanced checkpoint.

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
- Run-132 bridge `That lesson, rooted in her perseverance and responsibility, has deeply influenced how I address difficulties.`
- semantic chain: **patience -> perseverance -> responsibility -> changed behavior / stronger self**.

## Important recent experiments

- Run 119: third-paragraph `patience and responsibility` instead of `patience and perseverance`; **92.5**. Relevance collapsed to **72.2948**. Reject.
- Run 121: `Beyond this experience` instead of `Beyond that experience`; **94.0**, neutral. No gain.
- Run 122: conclusion `Taken together, these qualities ...`; **94.0**. Structure fell. Reject.
- Run 123: four-paragraph layout; **94.0**. Structure fell. Keep 3 paragraphs.
- Run 124: split concrete exam evidence into two short sentences; **93.0**. Structure rose to **91.1025**, but sentence fell to **89.3552**. Reject short-sentence optimization.
- Run 125: `a disappointing exam result that nearly made me give up`; **94.0**. Structure **90.7620**, relevance **91.0152**. Reject.
- Run 126: `a disappointing exam result that nearly made me lose confidence`; **94.0**. Relevance **90.2150**. Reject.
- Run 127: `Her example has made me resilient, responsible and considerate.`; **94.0**. Structure/relevance both fell. Reject.
- Run 129: `a disappointing grade at school that almost made me give up`; **94.0**. Reject.
- Run 130: `has exerted a profound influence on me far beyond that experience`; **93.5**. Vocabulary rose but sentence/relevance fell sharply. Reject advanced phrase stacking.
- Run 131: `she displays in supporting...`; **94.5**, equal checkpoint.
- **Run 132**: lesson-linked influence bridge; **94.5**, relevance **95.7044**. Promote.

## Diagnostic priority

On Run 132:
1. vocabulary **97.32** — excellent; do not chase rare vocabulary.
2. relevance **95.70** — now excellent; preserve this bridge and semantic chain.
3. sentence **93.45** — strong; small naturalness gains may matter.
4. structure **91.07** — weakest remaining dimension; target genuine cohesion, especially avoiding redundant transitions.

Do not optimize reference ranges mechanically. Forced short sentences, adjective-ratio changes, advanced phrase stacking, and explicit keyword repetition have all lowered headline score in prior tests.

## Infrastructure

- `.github/workflows/pigai-run.yml` triggers grading only when `essay.txt` changes (or manual dispatch).
- Successful grading creates artifacts containing `latest_feedback.json`, `latest_result.html`, `latest_result.png`, and `latest_essay.txt`.
- `LATEST_PIGAI_FEEDBACK.json` is convenient but not authoritative if post-grading persistence fails; inspect the artifact in that case.
- Documentation-only changes do not trigger a Pigai submission.

## Iteration rule

Start each new experiment from Run 132 unless a newer variant scores above **94.5**, or ties **94.5** with a clearly stronger balanced hidden profile. Preserve the Run-132 lesson bridge by default.

Only one primary linguistic variable per submission. If a variant scores below the active checkpoint, revert before the next experiment.

## Stop condition

**Stop only after a real Pigai result reports score >= 95.0.**
