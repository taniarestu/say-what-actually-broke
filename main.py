"""Entry for the make.fun "Say What Actually Broke" bounty.

Writes one text to /output/entry.txt. Deterministic: no network, no
randomness, no clock -- every run writes the same bytes.
The entry text is one fixed string, written below.
"""

import os
import sys

TEXT = """The database fell asleep mid-save and dropped your work. It is probably still in there somewhere. Refresh and try again."""


def main() -> None:
    path = sys.argv[1] if len(sys.argv) > 1 else "/output/entry.txt"
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
