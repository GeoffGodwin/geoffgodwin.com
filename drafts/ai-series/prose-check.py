#!/usr/bin/env python3
"""Mechanical voice checks for the AI series drafts.

Catches the failure modes found in the editing passes over part one. It flags
candidates for a human to judge rather than deciding anything itself, so a hit
is a prompt to reread a sentence, not a verdict on it.

Usage: python3 prose-check.py part-one-draft.mdx
"""
import re
import sys

# Deliberately conservative. An earlier version used a bare "un\w+" and matched
# "underneath", which buried the real hits in noise.
NEGATIONS = re.compile(
    r"(?:\bnot\b|n't\b|\bno\b|\bnone\b|\bnobody\b|\bnothing\b|\bnever\b"
    r"|\bneither\b|\bnor\b|\bwithout\b|\bcannot\b|\bfails? to\b|\blacks?\b"
    r"|\bun(?:able|likely|clear|aware|intended|supported|resolved|proven)\b"
    r"|\bin(?:capable|ability|sufficient|accessible|complete|correct)\b"
    r"|\bnon-\w+)",
    re.I,
)
BRITISH = re.compile(
    r"\b\w*(?:behaviour|organisation|organise|organising|organised|recognis|"
    r"optimis|realise|realising|analyse|analysing|analysed|"
    r"modelling|judgement|honour|maximis|rationalis|centre|licence)\w*\b",
    re.I,
)
LONG_SENTENCE = 45  # read anything past this out loud before shipping it


def strip_markup(text):
    text = re.sub(r"\[\^[a-z0-9-]+\]", "", text)
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)
    return re.sub(r"[#*_>`]", "", text)


def sentences_of(text):
    """Split prose into sentences, ignoring headings, rules and table rows."""
    lines = [
        ln for ln in text.split("\n")
        if ln.strip() and not ln.strip().startswith(("#", "---", "|", "> "))
    ]
    flat = " ".join(lines)
    # Split after terminal punctuation, including when it sits inside a closing
    # quote mark. Without the second alternative, a sentence ending on a quoted
    # phrase gets glued to the next one and reports a false over-length hit.
    return [
        s.strip()
        for s in re.split(r"(?<=[.?!][\"'”’])\s+|(?<=[.?!])\s+", flat)
        if s and len(s.split()) > 2
    ]


def main(path):
    raw = open(path, encoding="utf-8").read()
    prose = raw.split("---", 2)[2].split("\n[^")[0]
    clean = strip_markup(prose)

    print(f"== {path} ==\n")

    print("Word count by section")
    sections = re.split(r"\n## ", prose)
    names = ["(opening)"] + [s.split("\n")[0] for s in sections[1:]]
    total = 0
    for name, chunk in zip(names, sections):
        words = [w for w in strip_markup(chunk).split() if re.search(r"[A-Za-z0-9]", w)]
        total += len(words)
        print(f"  {len(words):5d}  {name}")
    print(f"  {total:5d}  TOTAL\n")

    sents = sentences_of(clean)

    print("Nested negation (rule 25). A comma-separated parallel list is fine.")
    hits = 0
    for s in sents:
        found = NEGATIONS.findall(s)
        # A deliberate parallel list carries about one comma per negative.
        if len(found) >= 2 and s.count(",") < len(found):
            hits += 1
            print(f"  [{len(found)}] {s[:150]}")
    if not hits:
        print("  none")

    print(f"\nSentences over {LONG_SENTENCE} words (read these aloud)")
    hits = 0
    for s in sents:
        n = len(s.split())
        if n > LONG_SENTENCE:
            hits += 1
            print(f"  [{n}w] {s[:150]}")
    if not hits:
        print("  none")

    print("\nBanned punctuation and spelling")
    print(f"  em dashes: {raw.count(chr(8212))}")
    print(f"  double hyphens in prose: {len(re.findall(r'(?<!-)--(?!-)', prose))}")
    brit = sorted({m.lower() for m in BRITISH.findall(raw)})
    print(f"  British spellings: {brit or 'none'}")
    matters = re.findall(r"\b\w+\s+matters[.,;]", raw)
    print(f"  'matters' as predicate: {matters or 'none'}")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "part-one-draft.mdx")
