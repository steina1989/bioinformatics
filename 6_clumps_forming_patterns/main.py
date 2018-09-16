#!/usr/bin/env python3
import sys
from bioutils import find_clumps


def main(dna, k, l, t):
    print(" ".join(find_clumps(dna, k, l, t)))


if __name__ == "__main__":
    dna = sys.stdin.readline().strip()
    K, L, T = map(int, sys.stdin.readline().strip().split())
    main(dna, K, L, T)
