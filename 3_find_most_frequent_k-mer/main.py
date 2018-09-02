#!/usr/bin/env python3
import sys
from bioutils import most_frequent_kmer

def main(dna,k):
    kmers = most_frequent_kmer(dna, k)
    print(' '.join(kmers))

if __name__ == '__main__':
    DNA = sys.stdin.readline().strip()
    K = sys.stdin.readline().strip()
    main(DNA,K)