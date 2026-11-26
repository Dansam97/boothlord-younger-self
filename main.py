#!/usr/bin/env python3
"""One Line to Your Younger Self — make.fun entry.

Writes a single line, in English, to /output/entry.txt: the one line the
writer would send back to their younger self. Gate: UTF-8 text of 1 to 200
characters, not only white space, a single line, no explanation, no second
sentence.
"""

import os

ENTRY = (
    "Stop hiding your report card in the piano bench \u2014 Mum already knows, "
    "and the lie will cost you more than the grades ever did."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = ENTRY.strip()
    if not (1 <= len(text) <= 200):
        raise ValueError(f"entry is {len(text)} chars, gate requires 1-200")
    if text != text.strip() or "\n" in text:
        raise ValueError("entry must be a single line with no surrounding whitespace")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)
    # Read back and re-check: a truncated or altered write must fail loudly
    # instead of shipping a gate-invalid entry.
    written = open(OUTPUT_PATH, encoding="utf-8").read()
    if written != text:
        raise ValueError("read-back mismatch: entry.txt does not match ENTRY")
    print(f"wrote {len(written)} chars to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
