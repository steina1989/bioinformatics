#!/usr/bin/env python3
import sys, collections
from operator import itemgetter
from bioutils import all_kmers, count_pattern_occurrence

"""
Assignment: Find the most frequent kmers in a dna string.

To do: Determine if this functionality belongs in bioutils and migrate if so.
"""

def main(dna, k):
    occurrence_dict = collections.defaultdict(int)
    for kmer in all_kmers(dna,k):
        occurrence_dict[kmer] += count_pattern_occurrence(dna,kmer)
    max_freq = max(occurrence_dict.values())
    filtered_dict = {k : v for k, v in occurrence_dict.items() if v == max_freq}
    print(' '.join(filtered_dict.keys()))

if __name__ == "__main__":
    DNA = sys.stdin.readline().strip()
    K = int(sys.stdin.readline().strip())
    main(DNA, K)
