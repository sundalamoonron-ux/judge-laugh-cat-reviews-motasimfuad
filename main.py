"""One-star cat review entry for make.fun.

Writes a single funny one-star review, written in the voice of a house
cat about its human, to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).

Gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters, not
only white space. The line below is deterministic: the same text is
written on every run.
"""

import os

ENTRY = "One star. Breakfast is at six. He calls my 3am reminder 'screaming'. I call it a calendar."


def _check_gate(line):
    """Refuse to write a line the sealed gate would reject."""
    if not 1 <= len(line) <= 200 or not line.strip():
        raise ValueError("entry line must be 1-200 characters, not only whitespace")


def main():
    _check_gate(ENTRY)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
