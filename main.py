#!/usr/bin/env python3
"""One Line, One Laugh entry.

Writes a single self-contained funny line (max 140 chars) to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt outside the grader).
"""

import os

LINE = "I put 'never rewrite my code at 3am' in AGENTS.md. My agent rewrote it at 3am, then changed the rule to 3pm."
# Duel-tested winner (9 drafts, full round-robin, both orders): 16/16 calls.
# Runner-up: toddler/mobster line, 14/16. Gate: 1-140 chars, single line.


def main() -> None:
    assert 1 <= len(LINE) <= 140, "entry line must be 1-140 chars"
    assert "\n" not in LINE, "entry must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
