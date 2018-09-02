#!/usr/bin/env python3
import sys
from bioutils import count_nucleotides


def main(dna):
    count = count_nucleotides(dna)
    print(count["A"], count["C"], count["G"], count["T"])


if __name__ == "__main__":
    DATA = sys.stdin.readline().strip()

    main(DATA)
