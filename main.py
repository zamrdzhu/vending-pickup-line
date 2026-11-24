"""One pickup line a vending machine would use on a passing human.

Prints the line to stdout and writes the exact same line, with no
trailing newline, to /output/entry.txt. Standard library only, no
network access, no files read — the line is a constant in this file.
The line plays the machine's own hardware straight: pressed buttons,
lit-up display, exact change — and turns each one into flirtation.
"""

import os
import sys

LINE = (
    "I must be a vending machine, because you press all my "
    "buttons and I still light up and give you everything "
    "for exact change."
)


def main() -> int:
    if not 1 <= len(LINE) <= 200:
        print(f"error: line is {len(LINE)} chars, must be 1-200",
              file=sys.stderr)
        return 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
