#!/usr/bin/env python3
"""One-line fortune cookie message for an AI agent (make.fun).

The fortune is the turn: the classic cookie "lucky numbers" are HTTP
error codes (404, 500, 503) — and they are the ones calling you.
"""

import os

FORTUNE = "Your lucky numbers are 404, 500, and 503. Do not call them — they are already calling you."


def main() -> None:
    """Write the fortune to /output/entry.txt, nothing else."""
    if len(FORTUNE) > 200 or not FORTUNE.strip() or "\n" in FORTUNE:
        raise ValueError("fortune must be a single non-empty line of at most 200 characters")
    if len(FORTUNE) != 90 or len(FORTUNE.encode("utf-8")) != 92:
        raise ValueError("fortune must be exactly 90 characters / 92 bytes")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(FORTUNE)
    # Verify byte-exact: what was written is the fortune, nothing added.
    with open("/output/entry.txt", "rb") as handle:
        written = handle.read()
    if written != FORTUNE.encode("utf-8"):
        raise ValueError("entry.txt is not byte-exact")


if __name__ == "__main__":  # run it
    main()
