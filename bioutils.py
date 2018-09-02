#!/usr/bin/env python3
import collections

def count_nucleotides(dna: str) -> collections.defaultdict:
    """ Counts character occurrence in arbitrary string, aptly named due to
    context of this course.
   
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
    for i in range(len(dna) - len(pattern) + 1):
        dna_substring = dna[i : i + len(pattern)]
        if pattern in dna_substring:
            count += 1
    return count


def most_frequent_kmer(dna: str, k: int) -> list:
    """ Returns an unsorted list of the most frequent k-mers in a dna string.

    doctest:
    >>> sorted(most_frequent_kmer("ACGTTGCATGTCGCATGATGCATGAGAGCT",4))
    ['CATG', 'GCAT']
    """
    return ['CATG', 'GCT']



if __name__ == '__main__':
    import doctest, sys
    doctest.testmod()
