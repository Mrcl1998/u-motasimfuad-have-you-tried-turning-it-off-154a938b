#!/usr/bin/env python3
"""Have You Tried Turning It Off? — one funny tech-support line.

Writes the entry to /output/entry.txt (1-199 chars, UTF-8, single line).
Pure standard library only.
"""

import os

ENTRY = (
    "Have you tried turning it off and on again? Say yes \u2014 "
    "my script doesn't have a button for 'no', and I've been "
    "stuck on this line since Tuesday."
)


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
