# Pigai High-Score Memory

> Persistent experiment memory for `essay.txt`. Read before editing. Preserve the best verified checkpoint, change one main variable per round, trust real Pigai A/B scores over intuition, and never keep a lower-scoring variant as baseline.

## Current best checkpoint

- Best verified score: **93.0**.
- Best role/topic: **grandmother**, with direct personal interaction and direct influence.
- Preferred best commit: `3229ac2ea48ec8c5f8b889f55fa021a33418f182` (Run 54).
- Run 54: 180 Pigai words; hidden dimensions vocabulary **0.9762753**, sentence **0.9082242**, structure **0.9028283**, relevance/cohesion **0.81538284**.
- No fragments/bad sentences. Pigai praised transitions, vocabulary/spelling, and complex syntax.
- After any losing experiment, restore this wording before testing another variable.

### Preferred 93.0 baseline text

```text
The person I hold in the highest regard is my grandmother, whose character, marked by patience, perseverance and responsibility, has left an indelible impression on me. What I admire most is the patience and responsibility with which she supports our family whenever difficulties arise.

For instance, I still remember when I performed poorly at school and wanted to give up. Instead of criticizing me, she spared no effort to encourage me and helped restore my confidence. She taught me to view difficulties as stepping stones to progress. More importantly, she taught me that perseverance matters most when circumstances are unfavorable, and that strength is shown through patience and responsibility.

Her example of perseverance and responsibility has exerted a profound influence on me far beyond that experience. Whenever I encounter setbacks, I follow her example, maintain my composure and continue moving forward rather than avoiding problems. Consequently, I have become more resilient, responsible and considerate. Ultimately, to me, she is not only the person I respect most, but also someone I will look up to and a constant source of strength.
```

## Preserve by default

- Pigai-recognized: **`far beyond`** = 闪光短语; **`spare no effort to`** = 精彩句型.
- `maintain my composure`: controlled gain **92.0 -> 92.5**.
- `exert a profound influence on ...`: helped **91.5 -> 92.0**.
- `patience, perseverance and responsibility`: major relevance improvement; preserve semantic chain.
- `Consequently,`, `Ultimately,`, `For instance,`: validated transitions. `For instance` produced the decisive **92.5 -> 93.0** gain.
- Also preserve unless directly A/B tested: `hold ... in the highest regard`, `leave an indelible impression on ...`, `view difficulties as stepping stones to progress`, `restore my confidence`, `a constant source of strength`, `look up to`, `with which ...`, `whenever difficulties arise`, `not only ... but also ...`.

## Experiment log

### Person/topic

- high-school teacher: ~**88.5**
- father: ~**90.5**
- mother: **91.0**
- grandmother: **93.0** best
- Yuan Longping/public figure: ~**88.5**

Inference: direct personal interaction beats a detached public figure for this task.

### Earlier phrase/structure tests

- `through thick and thin`: **91.0 -> 90.5**, reject.
- `in the face of difficulties`: **91.0**, no gain.
- mechanical repetition of perseverance/responsibility: **91.5 -> 90.5**, reject.
- `has exerted a profound influence on me`: **91.5 -> 92.0**, preserve.
- forced 11-sentence format: **92.0 -> 89.5**, reject.
- `true strength lies in`: **92.0 -> 91.5**, reject.
- `keep my composure` -> `maintain my composure`: **92.0 -> 92.5**, preserve.
- `change the way I face challenges`: **92.5 -> 92.0**, reject.
- `was tempted to give up`: **92.5**, weaker relevance, not preferred.
- `helped restore my confidence`: **92.5**, slightly better hidden metrics; preserve.
- `Thanks to her`: **92.5** but relevance fell, reject as preferred wording.
- `strength manifests itself through`: **92.5** but relevance fell, reject.
- `Rather than criticizing me`: **92.5 -> 92.0**, reject.
- `failed an important examination`: **92.5 -> 92.0**, reject.
- `almost lost confidence ... restore my confidence`: **92.5 -> 91.5**, reject.
- `guides me` replacing `supports our family`: **92.5 -> 92.0**, reject.
- `selflessness` -> `patience`: **92.5**, relevance rose ~0.767 -> **0.8174569**, preserve.
- `Because of her` -> `Consequently`: **92.5**, retained relevance and improved balance.
- add `Ultimately`: **92.5**, hidden metrics improved.
- add `For instance`: **92.5 -> 93.0**; Run 54 hidden dimensions vocab **0.9762753**, sentence **0.9082242**, structure **0.9028283**, relevance **0.81538284**.

### Runs 69–73, 2026-09-10

- **Run 69 / `f4ad8f7722e505947a42fcdcdf7e2cbd8bcb8fc6`**: concise direct-influence variant including `supports me whenever I face difficulties`; **93.0**, 175 words. Equal only; not promoted over Run 54.
- **Run 70 / `f20253d92363553bf6f49ff1301fa1c534559a92`**: from Run 54, changed present behavior to `face problems with patience and determination`; **93.0**, 179 words. Equal only; explicit patience link is tolerated but not a gain.
- **Run 71 / `f04b13c4d82e8f15e59876c3815028df07fbf55e`**: adjective-form opening triad `patient, persevering and responsible`; **91.5**, 178 words. Reject. Adjective share rose to 12% but score fell 1.5; do not optimize POS diagnostics mechanically.
- Restored preferred 93.0 baseline after Run 71 in `55467941c1cac11aa56a42dcfbb37106d651e134`.
- **Run 73 / `1b35e55606bd0cef711ccd25f804dbbc47fb7be6`**: replaced `She taught me to view difficulties as stepping stones to progress.` with explicit relevance sentence `That experience taught me why I respect her so deeply.`; **92.0**, 179 words. Reject. Directly repeating respect weakened the score and removed a validated high-value sentence.
- Restored preferred 93.0 baseline after Run 73 in `2577b0f014290a5d3af30e904202fd85ff70db23`.

### Run 120, 2026-09-10

- **Run 120 / `2e4a34220a37779496ae3d9db0854827b7d6bd6f`**: from the preferred Run 54 checkpoint, changed only the transition `More importantly,` to the experience-linked bridge `Through that experience,`; **93.0**, Pigai counted **181 words**. Hidden dimensions: vocabulary **0.974790**, sentence **0.910006**, structure **0.898570**, relevance **0.809743**. Equal headline score but weaker structure and relevance than Run 54, and it exceeded the stated 180-word limit by Pigai's counter. **Do not promote.** Keep Run 54 as preferred checkpoint and restore it before the next essay experiment.

## Diagnostic interpretation

- Vocabulary is already extremely strong; do not chase rare words.
- Run 54 sentence/structure scores are strong; explicit evidence bridge works.
- Relevance remains the weakest hidden dimension, but bluntly repeating `respect` does not help (Run 73).
- Run 120 shows that replacing `More importantly,` with a more explicit `Through that experience,` bridge does not improve the headline score and slightly weakens structure/relevance; keep the validated transition.
- Do not chase diagnostic reference ranges in isolation: forced 11 sentences and adjective-ratio optimization both caused large regressions.
- Keep 120–180 words; target 175–180, but never exceed 180.
- Preserve architecture: P1 person + qualities; P2 personal evidence; P3 concrete influence on behavior.
- Preserve semantic chain: **patience -> perseverance -> responsibility -> resilient/considerate behavior**.

## Infrastructure

- `.github/workflows/pigai-run.yml` grades every `essay.txt` push using the existing Pigai loop.
- Successful runs now persist `LATEST_PIGAI_FEEDBACK.json`, so the latest real score can be read directly without unpacking the artifact.
- Artifacts remain available for full HTML/screenshot inspection.

## Next hypotheses

- Focus on subtle cohesion/relevance changes that preserve all validated phrases; Run 70 shows explicit patience linkage is neutral, Run 73 shows explicit `respect` repetition is harmful, and Run 120 shows an experience-linked transition is also neutral/slightly weaker.
- Do not mechanically increase sentence count, adjective share, or rare vocabulary.
- Candidate experiments must start from the preferred Run 54 text and alter only one main variable.

## Stop condition

Target: **verified 98.0+** for the current optimization workflow. Do not claim success until a real Pigai run reports at least **98.0**.
