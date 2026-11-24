#!/usr/bin/env python3
"""Ridiculous at first glance, real by the second.

Writes exactly one line to /output/entry.txt and prints it.
Stdlib only. The twist flips the absurd image into a plausible paycheck.
"""

import os

LINE = "A man in a dinosaur suit directing traffic sounds absurd — until you learn he's the city's highest-paid crossing guard."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(LINE)


if __name__ == "__main__":
    main()
