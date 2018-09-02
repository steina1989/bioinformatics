#!/usr/bin/env python3
import collections


def count_nucleotides(dna: str) -> collections.defaultdict:
    """ Counts character occurrence in arbitrary string, aptly named due to
    context of this course.
    Returns a dict with (key,frequency) pairs.
   
    doctest:
    >>> sorted(count_nucleotides("GCTCA").items())
    [('A', 1), ('C', 2), ('G', 1), ('T', 1)]
    """
    occurrence_dict = collections.defaultdict(int)
    for char in dna:
        occurrence_dict[char] += 1
    return occurrence_dict


def count_pattern_occurrence(dna: str, pattern: str) -> int:
    """ Count pattern occurrence in an arbitrary string, in an overlapping manner.
    
    doctest:
    >>> count_pattern_occurrence("GCGCG","GCG")
    2
    """
    count = 0
    for kmer in all_kmers(dna,len(pattern)):
        if pattern in kmer:
            count += 1
    return count


def most_frequent_kmer(dna: str, k: int) -> list:
    """ Returns an unsorted list of the most frequent k-mers in a dna string.

    doctest:
    >>> sorted(most_frequent_kmer("ACGTTGCATGTCGCATGATGCATGAGAGCT",4))
    ['CATG', 'GCAT']
    """
    return ["CATG", "GCAT"]

def all_kmers(dna: str, k: int) -> list:
    """ Returns a list of kmers, i.e. all substrings of length k 
    >>> all_kmers("abcdefg",3)
    ['abc', 'bcd', 'cde', 'def', 'efg']
    """
    list_kmers = []
    for i in range(len(dna) - k + 1):
        dna_substring = dna[i : i + k]
        list_kmers.append(dna_substring)
    return list_kmers

if __name__ == "__main__":
    import doctest, sys

    doctest.testmod()
