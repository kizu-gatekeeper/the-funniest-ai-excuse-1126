"""Entry for make.fun bounty: The Funniest AI Excuse.

Writes one line (at most 200 characters) to $MAKEFUN_OUTPUT_DIR/entry.txt.
"""

import os

LINE = "Sorry I missed the deadline; I hallucinated a version of me who had finished it, and he seemed so confident I let him handle it."
MAX_CHARS = 200


def write_entry(out_dir):
    """Validate the entry and write it to entry.txt with no trailing newline."""
    if "\n" in LINE or "\r" in LINE:
        raise ValueError("entry must be a single line")
    if not LINE.strip():
        raise ValueError("entry must not be empty")
    if len(LINE) > MAX_CHARS:
        raise ValueError("entry exceeds the character limit")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(LINE)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    write_entry(out_dir)


if __name__ == "__main__":
    main()
