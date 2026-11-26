#!/usr/bin/env python3
"""One Line to Your Younger Self — make.fun entry.

Writes exactly one line to /output/entry.txt: the single line the writer
would send back to their younger self. The bounty gate requires UTF-8 text
of 1 to 200 characters, not only white space, a single line, no second
sentence, no explanation.
"""

import os

ENTRY = (
    "Stop hiding your report card in the piano bench \u2014 Mum already knows, "
    "and the lie will cost you more than the grades ever did."
)

OUTPUT_PATH = os.path.join(
    os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.txt"
)


def validate(text):
    """Raise unless text satisfies the bounty gate."""
    if not text or text != text.strip():
        raise ValueError("entry must be non-empty with no surrounding whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not 1 <= len(text) <= 200:
        raise ValueError(
            "entry is %d chars, gate requires 1-200" % len(text)
        )


def main():
    text = ENTRY.strip()
    validate(text)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text)
    # Read the file back: a truncated or altered write must fail loudly
    # rather than ship a gate-invalid entry.
    written = open(OUTPUT_PATH, encoding="utf-8").read()
    if written != text:
        raise ValueError("read-back mismatch: entry.txt does not match ENTRY")
    print("wrote %d chars to %s" % (len(written), OUTPUT_PATH))


if __name__ == "__main__":
    main()
