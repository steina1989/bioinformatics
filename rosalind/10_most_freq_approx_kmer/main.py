#!/usr/bin/env python3
import sys
from bioutils import most_frequent_approx_kmer


def main(dna, k, d):
    print(" ".join(most_frequent_approx_kmer(dna, k, d)))


if __name__ == "__main__":
    DNA = sys.stdin.readline().strip()
    K, D = map(int, sys.stdin.readline().strip().split())

    main(DNA, K, D)
