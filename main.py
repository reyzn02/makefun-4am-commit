#!/usr/bin/env python3
"""The 4AM Commit: Funniest Agent Bug-Fix Message.

The program writes one commit message to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt): the note an AI agent would leave in the log
after a long night of chasing down and fixing its own bugs. One line, at
most 200 characters, funny first and true to the machine voice second.

The joke is the agent's own condition: after a night of self-repair it
finally reads its own diff, discovers the bug is itself, reverts itself,
and is left with questions for itself in the morning. It uses only the
Python standard library, makes no network calls, and always writes the
same bytes.
"""

import os

LINE = (
    "fix: at 4am I finally read my own diff and found the bug: me. "
    "Reverted myself. Tests pass. I have questions for me in the morning."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = LINE.strip()
    if not (1 <= len(text) <= 200):
        raise SystemExit(f"entry must be 1-200 characters, got {len(text)}")
    if not text.strip():
        raise SystemExit("entry must not be only whitespace")
    if "\n" in text:
        raise SystemExit("entry must be a single line")
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
