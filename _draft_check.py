from pathlib import Path
import re


def count_words(text: str) -> int:
    return len([w for w in text.replace("\n", " ").split() if any(c.isalpha() for c in w)])


draft = """The person I hold in the highest regard is my grandmother. Her outstanding character, marked by patience, perseverance and responsibility, has left an indelible impression on me. Above all, I admire the patience and responsibility she displays in supporting our family whenever difficulties arise. Her steady devotion continues to guide my daily life.

To illustrate this, I vividly remember receiving a disappointing grade at school and wanting to give up. Instead of criticizing me, she spared no effort to encourage me and helped restore my confidence. She taught me to view difficulties as stepping stones to progress. Furthermore, I learned from her that perseverance matters most when life becomes difficult, and that strength is shown through patience and responsibility.

That valuable lesson, rooted in her perseverance and responsibility, has deeply influenced how I address difficulties. Whenever I encounter setbacks, I follow her example, maintain my composure and face challenges with patience and perseverance. Consequently, I have become more resilient, responsible and considerate. In conclusion, she is not only the person I respect most, but also someone I will look up to and a constant source of strength."""

print("words", count_words(draft))
sents = [s.strip() for s in re.split(r"(?<=[.!?])\s+", draft.replace("\n", " ")) if s.strip()]
print("sentences", len(sents))
for i, s in enumerate(sents, 1):
    print(f"{i:02d} ({count_words(s):02d}) {s}")
Path("essay.txt").write_text(draft + "\n", encoding="utf-8")
