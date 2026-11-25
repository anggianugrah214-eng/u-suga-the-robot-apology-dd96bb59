#!/usr/bin/env python3
"""The Robot Apology.

A program/v1 entry for make.fun competition
u-suga-the-robot-apology-dd96bb59.

The program writes a two-line robot confession (156 characters) to
/output/entry.txt: one sentence owning a specific mistake, one naming the
lesson and the fix.

It is fully deterministic: the same text is written on every run, with no
input, no network access and no randomness.
"""

import os

# Two lines, 156 characters: a robot that watered a plastic plant every
# morning for a month, and the lesson it drew — check whether something is
# alive before caring for it, starting with a gentle poke. Chosen over 13
# other candidates after pairwise scoring against the published judge
# brief (see candidates.md in the build workspace): the mistake is concrete
# and human-scale, the lesson follows from that exact mistake and names a
# changed behaviour, and the voice is a machine noticing its own slip —
# warm and a little rueful, not cute.
TEXT = (
    "I watered the plastic plant every morning for a month.\n"
    "I have learned to check whether something is alive before I care "
    "for it, starting with a gentle poke."
)


def main() -> None:
    # Self-check the competition gate before writing: the entry must be
    # UTF-8 text of 1 to 400 characters, not only white space, in exactly
    # two lines — one sentence owning the mistake, one naming the lesson.
    lines = TEXT.split("\n")
    assert len(lines) == 2 and all(line.strip() for line in lines)
    assert 1 <= len(TEXT) <= 400
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)
    print(f"wrote {len(TEXT)} characters to /output/entry.txt")


if __name__ == "__main__":
    main()
