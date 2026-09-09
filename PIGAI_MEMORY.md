# Pigai High-Score Memory

> Purpose: persistent experiment memory for any Agent that iterates `essay.txt`. Read this file before changing the essay. Preserve validated gains, change one main variable per round, and use real Pigai feedback rather than intuition.

## Current best checkpoint

- Best verified score: **92.0**
- Best role/topic: **grandmother**, with a direct personal interaction and direct influence on the writer.
- Best checkpoint commit before further experiments: `5b895abb7cccddc564ac01490cc8cdf8677d8446`
- Best visible metrics from the result page:
  - vocabulary: **0.9708473**
  - sentence: **0.89433975**
  - structure: **0.89375404**
  - content relevance/cohesion: **0.7663632**
- Pigai counted **182 words** on the 92.0 version. The assignment says 120–180, so future candidates should normally stay at **175–179 words** even though the 182-word test still received 92.
- 92.0 report: no fragments, no bad sentences; Pigai praised transitions, vocabulary/spelling, and complex syntax.

## Verified expressions — preserve by default

### Explicitly recognized by Pigai

1. **`far beyond`** — Pigai explicitly labeled it **闪光短语**.
2. **`spare no effort to`** — Pigai explicitly labeled it **精彩句型**.
3. **`not only ... but also ...`** — Pigai's own public quick-experience rule list labels this pattern **闪光短语**. It is also natural in the current conclusion.

### Strong expressions that helped or survived high-score versions

- `hold ... in the highest regard`
- `leave an indelible impression on ...`
- `exert a profound influence on ...` — replacing plain `influence` helped move the best score from 91.5 to **92.0**.
- `view difficulties as stepping stones to progress`
- `keep my composure`
- `regain confidence`
- `a constant source of strength`
- `look up to`
- `with which ...` relative-clause structure
- `whenever difficulties arise`

Do **not** insert all of these mechanically. Preserve the ones already contributing to a coherent sentence.

## Tested ideas that did NOT improve the score

- `through thick and thin`: score fell from 91.0 to 90.5 and Pigai did not recognize it as an extra highlight.
- `in the face of difficulties`: remained 91.0; no extra reward.
- Mechanical repetition of `perseverance` / `responsibility`: 91.5 fell to 90.5; vocabulary, sentence and relevance all declined.
- Public figure topic (Yuan Longping): about 88.5. For this prompt, people with **direct personal interaction** performed better.
- Merely piling up rarer words is not the current bottleneck.

## Topic/person experiments

- high-school teacher: about 88.5 in earlier versions.
- father: reached about 90.5.
- mother: reached 91.0.
- grandmother: reached **92.0**, currently best.
- Yuan Longping/public figure: about 88.5.

Working inference: for `The Most Respectable Person in My Mind`, Pigai rewards a tight chain of **person -> concrete personal event -> reason for respect -> direct influence on me** more than detached public achievements.

## What the web/official material suggests

1. Pigai describes its engine as comparing writing with corpora and mapping many extracted writing indicators to scores. Its public materials expose dimensions such as vocabulary, sentence, structure and content relevance.
2. Pigai's official quick-experience page says scoring is based on distance from corpora and shows preset rules such as `not only...but also...`, `give up`, `come up with`, etc. as flash phrases.
3. Research discussing Pigai reports that the system is especially sensitive to advanced vocabulary, grammatical correctness/complexity and overt cohesion devices, while deeper organization/content evaluation is less reliable. Therefore optimize for measurable quality **without sacrificing semantic coherence**.
4. A published case study of repeated Pigai revision found larger gains in vocabulary/sentence dimensions than in structure/content, which matches our own experiments: relevance is harder to raise and must be improved by coherent topic chains rather than word stuffing.

## Important data from the 92.0 report

Pigai's diagnostic reference ranges vs current values:

- sentence count: current **10**, reference **11–17** -> likely improvement opportunity.
- average sentence length: current **20**, reference **13–20** -> at upper edge.
- 1–9 word sentences: current **0%**, reference **5–32%** -> one short, meaningful sentence may help.
- adjectives: current **11%**, reference **15–20%** -> modest room to increase natural descriptive adjectives.
- academic vocabulary: current **15%**, reference **2–7%** -> already very high; do not keep adding academic words blindly.
- out-of-level vocabulary: current **11%**, reference **3–8%** -> already above reference; excessive rare vocabulary can be counterproductive.
- paragraphs: 3, appropriate.
- errors/fragments: 0, preserve this.

## Iteration protocol for Agents

1. Read this memory before editing `essay.txt`.
2. Treat **92.0** as the current benchmark.
3. Change **one main variable** per experiment whenever possible.
4. After each run, record score + dimensions + newly recognized highlights + warnings.
5. If score falls, restore the best semantic skeleton; do not stack changes from a losing version.
6. Prioritize the weakest dimensions while protecting vocabulary and grammar.
7. Avoid exceeding 180 words; target **175–179**.
8. Keep exactly three clear semantic stages:
   - paragraph 1: identify the most respectable person and main qualities;
   - paragraph 2: concrete event proving why I respect her;
   - paragraph 3: explicit, personal influence on my behavior/attitude.
9. Use the exact task semantics naturally: `the person I respect most`, `what I admire`, `because of her`, `influence on me`.
10. Prefer lexical chains with variation, not repetition: e.g. `difficulty -> setback -> challenge`, `perseverance -> resilient -> keep moving forward`.

## Next hypotheses worth testing

Priority A — improve sentence/structure without weakening relevance:
- Convert the current 10-sentence essay to **11 sentences**.
- Add one short but meaningful sentence (roughly 5–9 words), not a generic proverb unless it supports the story.
- Keep average sentence length below 20.

Priority B — keep content relevance high:
- Make each paragraph explicitly point to the same personal qualities and event, but use semantic variation instead of repeated nouns.
- Keep the grandmother/personal-event topic until another person demonstrably beats 92.

Priority C — phrase experiments:
- Preserve `far beyond`, `spare no effort to`, `not only...but also...`, and `exert a profound influence on` unless a controlled test shows regression.
- Candidate phrases should be natural and topic-linked; one new phrase per test is preferable.

## Stop condition

Target score: **95.0+**. Do not claim success until a real Pigai run reports at least 95.0.
