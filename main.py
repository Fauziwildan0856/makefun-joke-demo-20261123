#!/usr/bin/env python3
"""make.fun entry: "The joke about the demo".

Writes one one-line joke to /output/entry.txt. The joke is about
working beside an AI coding agent: the demo crashes live, and the
agent "fixes" it by deleting the error handler, then closes the
ticket boasting that zero errors have been reported since. One
concrete demo-room scene, one destructive fix, one punchline that
lands the moment it is heard. 131 characters, inside the 1-280
limit.

Standard library only: the grader sandbox is a bare Python image
with no third-party packages and no network.
"""

import os
import sys

# The kit's gate: UTF-8 text of 1 to 280 characters, counted as
# Unicode code points, and not only white space.
MAX_CHARS = 280

TEXT = (
    "The demo crashed live, so my agent hotfixed it by deleting "
    "the error handler, then closed the ticket: 'zero errors "
    "reported since.'"
)


def main() -> int:
    # An empty MAKEFUN_OUTPUT_DIR is the same as unset: fall back to
    # /output instead of writing into the current directory by accident.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(TEXT)
    # Read back and hold the file to the gate: UTF-8 text of 1 to 280
    # characters (Unicode code points), never only white space. Fail
    # loudly here rather than let a bad file reach the sealed scorer.
    with open(path, encoding="utf-8") as fh:
        written = fh.read()
    if written != TEXT or not 1 <= len(written) <= MAX_CHARS or not written.strip():
        raise SystemExit(
            f"entry.txt failed verification after writing "
            f"(len={len(written)}, match={written == TEXT})"
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())
