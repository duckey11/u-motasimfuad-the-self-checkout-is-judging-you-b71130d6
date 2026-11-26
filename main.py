"""Self-checkout machine entry.

Deterministic: writes one fixed judgmental one-liner to /output/entry.txt.
No randomness, no time, no network, no external files.
"""

import os

LINE = (
    "Twelve energy drinks, one banana, and a candle that smells like "
    "'fresh linen.' You are not grocery shopping. "
    "You are staging a cry for help."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
