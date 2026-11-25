#!/usr/bin/env python3
"""The Funniest Honest Appliance Error.

Writes one line -- the funniest honest error message an appliance could
show -- to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output) and prints the
same line to stdout.

Deterministic: no network, no randomness, no clock.
"""

import os
import sys

ENTRY = (
    "Error E7: unbalanced load. You put one shoe in me and expected a "
    "fair fight. Add a second shoe, or accept the wobble."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")
    os.chmod(path, 0o644)
    print(ENTRY)


if __name__ == "__main__":
    sys.exit(main())
