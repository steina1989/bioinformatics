#!/usr/bin/env python3
import sys
from bioutils import approximate_occurrences


def main(dna, pattern, d):
    print(" ".join(map(str, approximate_occurrences(dna, pattern, d))))


if __name__ == "__main__":
    PATTERN = sys.stdin.readline().strip()
    DNA = sys.stdin.readline().strip()
    D = int(sys.stdin.readline().strip())

    main(DNA, PATTERN, D)
