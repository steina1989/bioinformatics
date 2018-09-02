#!/usr/bin/env python3
import sys
from 2_count_pattern_occurrence import count_pattern_occurrence

def most_frequent_kmer(dna: str, k: int) -> list:
    """ Returns an unsorted list of the most frequent k-mers in a dna string.
    >>> sorted(most_frequent_kmer("ACGTTGCATGTCGCATGATGCATGAGAGCT",4))
    ['CATG', 'GCAT']
    """
    for i in range(l)
    count
    # return ['CATG', 'GCAT']

if __name__ == "__main__":

    import doctest

    doctest.testmod()

    """ Pipe dataset in via terminal.
    The i/o format conforms to Rosalind's excercise provided i/o format.
    """
    DNA = sys.stdin.readline().strip()
    K = sys.stdin.readline().strip()
    kmers = most_frequent_kmer(DNA, K)
    print(' '.join(kmers))
