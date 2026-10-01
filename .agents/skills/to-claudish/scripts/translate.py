#!/usr/bin/env python3
"""Rewrite one chunk of plain English as Claudish."""

from __future__ import annotations

import sys

import programasweights as paw


PROGRAM_ID = "ca9d5165b6c8e6615529"


def main() -> int:
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} TEXT", file=sys.stderr)
        return 2

    translate = paw.function(PROGRAM_ID)
    print(translate(sys.argv[1]))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
