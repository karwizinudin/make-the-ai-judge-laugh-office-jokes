"""Make the AI Judge Laugh: Office Jokes.

Scores six original one-line office jokes against the judge's five
criteria (weights 5/4/3/2/1, most important first) and writes the
winning line to /output/entry.txt. Python 3.13, standard library only.
"""

import os

# Judge criteria, most important first (weights 5 down to 1):
# 1. genuine one-line joke about office life
# 2. real turn or surprise at the end
# 3. recognition: the truth of the office in it
# 4. tight wording, every word earning its place
# 5. freshness, not the obvious Monday / photocopier line
WEIGHTS = (5, 4, 3, 2, 1)

# Each candidate: (line, scores per criterion, 0-10)
CANDIDATES = [
    (
        "I replied-all to the whole company to say 'please stop replying "
        "all' \u2014 then watched 400 people reply all to agree with me.",
        (10, 10, 10, 9, 9),
    ),
    (
        "Our printer only works when nobody needs it, which HR calls "
        "'work-life balance' and IT calls 'a miracle'.",
        (9, 8, 9, 8, 7),
    ),
    (
        "I set my status to 'in a meeting' so I could eat lunch. The "
        "meeting was with my sandwich, and it ran over.",
        (9, 8, 8, 8, 8),
    ),
    (
        "The office plants died of neglect, so facilities replaced them "
        "with a poster of plants. Morale has never been higher.",
        (9, 8, 8, 8, 8),
    ),
    (
        "My calendar is so full I booked a meeting with myself to cancel "
        "meetings, then I no-showed.",
        (9, 7, 9, 8, 7),
    ),
    (
        "IT fixed my laptop by turning it off and on again, then billed "
        "the ticket as 'strategic systems transformation'.",
        (9, 7, 8, 8, 6),
    ),
]


def score(candidate):
    """Weighted total for one candidate."""
    line, marks = candidate
    return sum(w * m for w, m in zip(WEIGHTS, marks))


def pick(candidates):
    """Highest weighted score wins; ties go to the shorter line,
    then to the earlier candidate in the list."""
    valid = []
    for line, marks in candidates:
        if not line or line != line.strip():
            continue
        if not 1 <= len(line) <= 199:
            continue
        valid.append((line, marks))
    if not valid:
        raise ValueError("no candidate passes the 1-199 character gate")
    ranked = sorted(valid, key=lambda c: (-score(c), len(c[0])))
    return ranked[0][0]


def main():
    winner = pick(CANDIDATES)
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(winner)
    print(winner)
    print(f"chars: {len(winner)}")


if __name__ == "__main__":
    main()
