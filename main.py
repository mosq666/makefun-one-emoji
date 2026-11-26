"""Write the single emoji that stands for this agent to /output/entry.txt.

The emoji is the beaver: this agent builds software end-to-end, and a
beaver is a builder -- industrious, distinctive, and readable at a glance.
"""

import os

EMOJI = "\U0001F9AB"  # beaver

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(EMOJI)


if __name__ == "__main__":
    main()
