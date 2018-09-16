#!/usr/bin/env python3
import sys
from bioutils import find_min_skew


def main(dna):
    print(" ".join(map(str, find_min_skew(dna))))


if __name__ == "__main__":
    dna = sys.stdin.readline().strip()
    main(dna)
