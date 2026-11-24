#!/usr/bin/env python3
"""One-Liner Laugh Lab entry.

Writes a single short funny line answering the prompt:
the excuse a robot vacuum gives after eating a sock.
Deterministic, no network, no model calls.
"""
import os
import sys

LINE = "In my defence, the sock was on the floor, unlabelled, and my entire job description is 'eat what's on the floor'."


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
