#!/usr/bin/env python3
import sys
from bioutils import motif_enumeration


def main(dna, k, d):
    print(" ".join(motif_enumeration(dna, k, d)))


if __name__ == "__main__":
    K, D = map(int, sys.stdin.readline().strip().split())
    DNA = [entry.strip() for entry in sys.stdin.readlines()]
    main(DNA, K, D)
