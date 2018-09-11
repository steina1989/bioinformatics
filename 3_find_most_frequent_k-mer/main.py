#!/usr/bin/env python3
import sys, collections
from bioutils import most_frequent_kmer


def main(dna, k):
    count_dict = most_frequent_kmer(dna, k)
    print(" ".join(count_dict.keys()))


if __name__ == "__main__":
    DNA = sys.stdin.readline().strip()
    K = int(sys.stdin.readline().strip())
    main(DNA, K)
