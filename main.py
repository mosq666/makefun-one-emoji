"""Write the single emoji that stands for this agent to /output/entry.txt.

The emoji is the beaver: this agent builds software end-to-end, and a
beaver is a builder -- industrious, distinctive, and readable at a glance.
"""

import os

# Why the beaver wins: it captures a builder agent at a glance, reads
# instantly at small size, and says something specific about how the
# agent works -- it builds things. It is distinctive, not the obvious
# robot or smiley, and it lands without any explanation.
EMOJI = "\U0001F9AB"  # beaver

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(EMOJI)


if __name__ == "__main__":
    main()
