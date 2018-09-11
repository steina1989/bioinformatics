#!/usr/bin/env python3
import sys
from bioutils import find_pattern_indexes


def main(pattern, dna):
    print(" ".join(list(map(str, find_pattern_indexes(dna, pattern)))))


if __name__ == "__main__":
    PATTERN = sys.stdin.readline().strip()
    DNA = sys.stdin.readline().strip()
    main(PATTERN, DNA)
