#!/usr/bin/env python3
"""Notes From a Passive-Aggressive Fridge.

Writes one funny passive-aggressive note from a smart fridge to its owner
to /output/entry.txt. Deterministic, offline, stdlib only.

The note: a single line, dry, petty and specific — the fridge as a smug,
judgmental roommate that knows exactly what you ate and when.
"""

import os

# The note the fridge leaves on its door screen. One line, no trailing
# newline, so the gate counts exactly the characters of the note itself.
# The joke turns twice: the fridge counted the bites (interior camera),
# then reveals it is not just holding the footage — it IS the footage.
NOTE = "That 'one bite' of cake was four bites. I have the footage. I am the footage."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(NOTE)


if __name__ == "__main__":
    main()
