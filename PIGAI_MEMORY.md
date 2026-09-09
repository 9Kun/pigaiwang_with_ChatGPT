# Pigai High-Score Memory

> Persistent experiment memory for any Agent that iterates `essay.txt`. **Read this file before editing the essay.** Preserve validated gains, change one main variable per round, and trust real Pigai A/B results over intuition.

## Current best checkpoint

- Best verified score: **93.0**
- Best role/topic: **grandmother**, with direct personal interaction and direct influence on the writer.
- Best verified 93.0 commit: `3229ac2ea48ec8c5f8b889f55fa021a33418f182` (Run 54).
- Pigai word count: **180**, exactly at the task limit of 120–180. Any new phrase must replace or remove words elsewhere.
- Hidden dimensions for Run 54:
  - vocabulary: **0.9762753**
  - sentence: **0.9082242**
  - structure: **0.9028283**
  - content relevance/cohesion: **0.81538284**
- Report: no fragments or bad sentences; Pigai praised transitions, vocabulary/spelling, and complex syntax.

### Preferred 93.0 baseline text

```text
The person I hold in the highest regard is my grandmother, whose character, marked by patience, perseverance and responsibility, has left an indelible impression on me. What I admire most is the patience and responsibility with which she supports our family whenever difficulties arise.

For instance, I still remember when I performed poorly at school and wanted to give up. Instead of criticizing me, she spared no effort to encourage me and helped restore my confidence. She taught me to view difficulties as stepping stones to progress. More importantly, she taught me that perseverance matters most when circumstances are unfavorable, and that strength is shown through patience and responsibility.

Her example of perseverance and responsibility has exerted a profound influence on me far beyond that experience. Whenever I encounter setbacks, I follow her example, maintain my composure and continue moving forward rather than avoiding problems. Consequently, I have become more resilient, responsible and considerate. Ultimately, to me, she is not only the person I respect most, but also someone I will look up to and a constant source of strength.
```

## Verified expressions — preserve by default

### Explicitly recognized by this Pigai task

1. **`far beyond`** — explicitly labeled **闪光短语** by Pigai.
2. **`spare no effort to`** — explicitly labeled **精彩句型** by Pigai.

### Controlled A/B gains

- **`maintain my composure`** — replacing `keep my composure` raised **92.0 -> 92.5**; preserve.
- **`exert a profound influence on ...`** — helped **91.5 -> 92.0**; preserve.
- **`patience` quality chain** — replacing one-off `selflessness` with `patience` kept 92.5 but raised hidden relevance dramatically from about **0.767 -> 0.817**. Preserve `patience, perseverance and responsibility`.
- **`Consequently,`** — on the high-relevance patience baseline retained relevance **0.8174569** while restoring structure/vocabulary; preserve unless a later A/B beats it.
- **`Ultimately,`** — retained 92.5 and improved hidden metrics: vocab **0.9762782**, sentence **0.90292885**, structure **0.8982254**, relevance **0.8174569**.
- **`For instance,`** — adding an explicit reason-to-example bridge on the strongest 92.5 baseline raised the real score to **93.0**. This is the current decisive positive structural change.

### Strong expressions that survive the best version

- `hold ... in the highest regard`
- `leave an indelible impression on ...`
- `view difficulties as stepping stones to progress`
- `restore my confidence`
- `a constant source of strength`
- `look up to`
- `with which ...`
- `whenever difficulties arise`
- `not only ... but also ...`

Do **not** insert phrases mechanically. A phrase is useful only when it preserves the person -> reason -> personal evidence -> influence semantic chain.

## Web / official Pigai findings

1. Pigai publicly describes scoring as measuring essay/corpus distance and mapping writing indicators to a score.
2. Pigai's public quick-experience page shows task formulas can be configured. Public preset flash phrases are candidate generators only; they are not guaranteed active in this assignment.
3. `change the way` was a public example but scored **92.5 -> 92.0** here, confirming task-specific A/B testing is essential.
4. Published analyses and our own experiments both suggest Pigai responds strongly to advanced vocabulary, grammatical complexity, and overt cohesion. Vocabulary is already near 98%; current leverage is mostly structure/cohesion and content relevance.

## Experiment log

### Topic/person experiments

- high-school teacher: about **88.5**
- father: about **90.5**
- mother: **91.0**
- grandmother: **93.0**, current best
- Yuan Longping/public figure: about **88.5**

Working inference: for this prompt, a person with direct personal interaction performs better than a detached public figure.

### Important phrase / structure experiments

- `through thick and thin`: **91.0 -> 90.5**; reject.
- `in the face of difficulties`: stayed **91.0**; no gain.
- mechanical repetition of `perseverance` / `responsibility`: **91.5 -> 90.5**; reject.
- `has exerted a profound influence on me`: **91.5 -> 92.0**; preserve.
- forced 11-sentence format: **92.0 -> 89.5**; reject. Do not game diagnostic ranges mechanically.
- `true strength lies in`: **92.0 -> 91.5**; reject.
- `keep my composure` -> `maintain my composure`: **92.0 -> 92.5**; preserve.
- `change the way I face challenges`: **92.5 -> 92.0**; reject.
- `was tempted to give up`: stayed 92.5 but had weaker relevance than preferred baseline; not preferred.
- `helped restore my confidence`: stayed 92.5 and slightly improved hidden metrics versus `helped me regain confidence`; preserve.
- `Thanks to her`: stayed 92.5 but relevance fell; reject as preferred wording.
- `strength manifests itself through`: stayed 92.5 but relevance fell; reject.
- `Rather than criticizing me`: **92.5 -> 92.0**; reject.
- `failed an important examination`: **92.5 -> 92.0**; reject.
- `almost lost confidence ... restore my confidence`: **92.5 -> 91.5**; reject mechanical semantic repetition.
- `guides me` replacing `supports our family`: **92.5 -> 92.0**; reject.
- `selflessness` -> `patience`: stayed **92.5**, but relevance rose to **0.8174569**; major hidden-metric gain, preserve.
- `Because of her` -> `Consequently`: stayed **92.5**, kept relevance 0.8174569 and improved balance; preserve.
- add `Ultimately` before conclusion: stayed **92.5**, hidden dims improved to vocab 0.9762782 / sentence 0.90292885 / structure 0.8982254 / relevance 0.8174569.
- add `For instance` before the personal anecdote: **92.5 -> 93.0**. Hidden dims: vocab **0.9762753**, sentence **0.9082242**, structure **0.9028283**, relevance **0.81538284**. This is the current best real score.

## Current diagnostic interpretation

Run 54 / 93.0:

- vocabulary **97.63%** — extremely high; do not chase obscure vocabulary blindly.
- sentence **90.82%** — strongest sentence score so far among preferred checkpoints.
- structure **90.28%** — explicit evidence bridge was highly effective.
- content relevance **81.54%** — still the lowest dimension, but far above the old ~76% plateau.
- word count **180** — hard ceiling; new additions require cuts/replacements.
- sentence count **10**; reference says 11–17, but forcing 11 caused a major regression.
- fragments **0**, bad sentences **0**.

## Iteration protocol for Agents

1. Read this memory before editing `essay.txt`.
2. Treat **93.0 / Run 54** as the benchmark until a real Pigai run beats it.
3. Change one main variable per experiment whenever possible.
4. After each run, record real score and hidden dimensions when available.
5. If score falls, restore the best checkpoint; never stack changes from a losing version.
6. Keep final essay **<=180 words**. Current baseline is exactly 180, so additions require compensating cuts.
7. Preserve the three-stage architecture:
   - P1: identify grandmother + qualities;
   - P2: explicit example proving why she is respected;
   - P3: explicit influence on attitudes/behavior.
8. Preserve the high-relevance semantic chain: **patience -> perseverance -> responsibility -> resilient/considerate behavior**.
9. Prefer semantic variation over mechanical repetition.
10. Do not optimize a diagnostic reference range in isolation.

## Next hypotheses worth testing

Priority A — increase relevance without destroying Run 54 structure:
- test a more personal but natural variant of `supports our family` only if it preserves the patience quality chain; previous `guides me` failed, so use caution.
- test micro-edits in P3 that connect grandmother's qualities to present behavior without repeating exact keywords.

Priority B — structure/sentence micro-gains while staying <=180:
- preserve `For instance`, `Consequently`, `Ultimately` unless a controlled A/B beats them.
- candidate transition replacements should not add words unless a compensating cut is made.

Priority C — task-verified high-value phrases:
- preserve `far beyond`, `spare no effort to`, `maintain my composure`, and `exert a profound influence on`.

## Stop condition

Target score: **95.0+**. Do not claim success until a real Pigai run reports at least **95.0**.
