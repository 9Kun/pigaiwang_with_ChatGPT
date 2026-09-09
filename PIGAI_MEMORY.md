# Pigai High-Score Memory

> Persistent experiment memory for any Agent that iterates `essay.txt`. **Read this file before editing the essay.** Preserve validated gains, change one main variable per round, and trust real Pigai A/B results over intuition.

## Current best checkpoint

- Best verified score: **92.5**
- Best role/topic: **grandmother**, with direct personal interaction and direct influence on the writer.
- Best verified 92.5 commit: `9406b92c64b3cba0242f83969bfb0f2820303aae` (Run 40).
- Pigai word count: **179**, safely within the task limit of 120–180.
- Hidden dimensions for the preferred 92.5 baseline:
  - vocabulary: **0.9747575**
  - sentence: **0.9026788**
  - structure: **0.89570724**
  - content relevance/cohesion: **0.7662771**
- Report: no fragments or bad sentences; Pigai praised transitions/cohesion, vocabulary/spelling and complex syntax.

### Preferred 92.5 baseline text

```text
The person I hold in the highest regard is my grandmother, whose character, marked by selflessness, perseverance and responsibility, has left an indelible impression on me. What I admire most is the patience and responsibility with which she supports our family whenever difficulties arise.

I still remember when I performed poorly at school and wanted to give up. Instead of criticizing me, she spared no effort to encourage me and helped me regain confidence. She taught me to view difficulties as stepping stones to progress. More importantly, she taught me that perseverance matters most when circumstances are unfavorable, and that strength is shown through patience and responsibility.

Her example of perseverance and responsibility has exerted a profound influence on me far beyond that experience. Whenever I encounter setbacks, I follow her example, maintain my composure and continue moving forward rather than avoiding problems. Because of her, I have become more resilient, responsible and considerate. To me, she is not only the person I respect most, but also someone I will look up to and a constant source of strength.
```

## Verified expressions — preserve by default

### Explicitly recognized by this Pigai task

1. **`far beyond`** — explicitly labeled **闪光短语** by Pigai.
2. **`spare no effort to`** — explicitly labeled **精彩句型** by Pigai.

### Controlled A/B gains

- **`maintain my composure`** — replacing `keep my composure` on the legal 92.0 baseline raised the real score to **92.5**. This is a verified positive phrase and should be preserved.
- **`exert a profound influence on ...`** — upgrading plain `influence` previously helped move the best score from 91.5 to **92.0**.

### Strong expressions that survive the best version

- `hold ... in the highest regard`
- `leave an indelible impression on ...`
- `view difficulties as stepping stones to progress`
- `regain confidence`
- `a constant source of strength`
- `look up to`
- `with which ...`
- `whenever difficulties arise`
- `not only ... but also ...`

Do **not** insert phrases mechanically. A phrase is useful only when it preserves the person -> event -> reason -> influence semantic chain.

## Web / official Pigai findings

1. Pigai publicly describes scoring as measuring the distance between an essay and corpora and mapping extracted writing indicators to a score.
2. Pigai's public quick-experience page shows that scoring rules/formulas can be configured for a task. It lists examples such as `change the way`, `give up`, `not only...but also...`, `come up with`, etc. as preset flash phrases.
3. **Important task-specific lesson:** a public preset is not guaranteed to be active in this exact assignment. We tested `change the way` on the 92.5 baseline; the page still showed only one flash phrase and the score fell to 92.0. Therefore only this assignment's real A/B results count as validated.
4. Published analyses of Pigai report stronger sensitivity to advanced vocabulary, grammatical complexity and overt cohesion than to deep content/organization. Our own experiments agree: vocabulary is already very high, while relevance remains the hardest dimension to raise.

## Experiment log

### Topic/person experiments

- high-school teacher: about **88.5**
- father: about **90.5**
- mother: **91.0**
- grandmother: **92.5**, current best
- Yuan Longping/public figure: about **88.5**

Working inference: for this prompt, a person with **direct personal interaction and direct influence on me** performs better than a detached public figure.

### Phrase / structure experiments

- `through thick and thin`: **91.0 -> 90.5**, not recognized; reject.
- `in the face of difficulties`: stayed **91.0**; no gain.
- mechanical repetition of `perseverance` / `responsibility`: **91.5 -> 90.5**; reject.
- stronger lexical cohesion/semantic bridge: helped relevance rise substantially and produced **91.5**.
- `has exerted a profound influence on me`: **91.5 -> 92.0**; preserve.
- 182-word 92.0 version: high score but outside stated limit; do not use as final.
- 11-sentence / short sentence experiment (`Her actions speak louder than words.`): **92.0 -> 89.5**; reject. Do not game diagnostic reference ranges mechanically.
- first 179-word trim that weakened several phrases: **92.0 -> 91.5**; reject.
- controlled 179-word trim (`I still remember when...`; `she taught me...`): retained **92.0**; legal baseline.
- `true strength lies in`: **92.0 -> 91.5**; reject.
- `keep my composure` -> **`maintain my composure`**: **92.0 -> 92.5**; verified gain.
- `Because of her, I have changed the way I face challenges.`: **92.5 -> 92.0**; reject for this task despite public quick-experience examples.
- `I still remember ... wanted to give up` -> `I remember ... was tempted to give up`: stayed **92.5**. Hidden dimensions changed to vocab **0.9761274**, sentence **0.9014356**, structure **0.90017426**, relevance **0.7624047**. Because relevance is the main bottleneck and fell slightly, prefer the Run 40 wording.

## Current diagnostic interpretation

Preferred 92.5 baseline (Run 40):

- vocabulary **97.48%** — already extremely high; do not chase rare words blindly.
- sentence **90.27%** — strong but still has room for natural collocation upgrades.
- structure **89.57%** — strong; preserve the current three-paragraph architecture.
- content relevance **76.63%** — lowest dimension and hardest bottleneck.

Visible report characteristics:

- word count: **179**
- sentence count: **10**; reference page says 11–17, but forcing 11 sentences caused a large regression.
- average sentence length: **20**, upper edge of reference range.
- fragments: **0**
- bad sentences: **0**
- academic vocabulary and out-of-level vocabulary are already above reference ranges, so additional obscure words can hurt rather than help.

## Iteration protocol for Agents

1. Read this memory before editing `essay.txt`.
2. Treat **92.5 / Run 40** as the benchmark until a real Pigai run beats it.
3. Change **one main variable** per experiment whenever possible.
4. After each run, record score, hidden dimensions when available, newly recognized highlights, and any warnings/errors.
5. If score falls, restore the preferred baseline; never stack changes from a losing version.
6. Keep the essay at **175–179 words**; never knowingly exceed 180 for the final candidate.
7. Preserve the three-stage semantic architecture:
   - P1: identify the person and qualities;
   - P2: concrete personal event proving why I respect her;
   - P3: explicit direct influence on my attitudes/behavior.
8. Preserve exact task semantics naturally: `the person I respect most`, `What I admire most`, `Because of her`, `influence on me`.
9. Prefer semantic variation over repeated keywords: `difficulty -> setback`, `perseverance -> resilient -> continue moving forward`.
10. Do not optimize a diagnostic reference range in isolation. The 11-sentence experiment proved that local metric matching can reduce the actual score.

## Next hypotheses worth testing

Priority A — natural collocation micro-upgrades on the 92.5 baseline:

- `helped me regain confidence` -> `helped restore my confidence` (same approximate length; stronger collocation candidate).
- `Because of her` -> `Thanks to her` (same three-word causal bridge; positive relation, but must be A/B tested).
- other upgrades should change only one phrase and preserve all verified expressions.

Priority B — relevance:

- improve direct personal influence without removing `resilient, responsible and considerate`, which performed better than the `change the way` replacement.
- keep the grandmother + personal failure/support story unless another topic beats **92.5** in a real run.

Priority C — flash phrases:

- preserve task-verified `far beyond` and `spare no effort to`.
- public Pigai flash-phrase lists are candidate generators only, not proof of reward in this task.

## Stop condition

Target score: **95.0+**. Do not claim success until a real Pigai run reports at least **95.0**.
