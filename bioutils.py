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
    k = len(pattern)
    for kmer in all_kmers(dna, k):
        if pattern in kmer:
            count += 1
    return count


def most_frequent_kmer(dna: str, k: int) -> list:
    """Returns an unsorted list of the most frequent k-mers in a dna string.
    
    doctest:
    >>> sorted(most_frequent_kmer("ACGTTGCATGTCGCATGATGCATGAGAGCT",4))
    ['CATG', 'GCAT']
    """
    occurrence_dict = collections.defaultdict(int)
    for i in range(len(dna) - k + 1):
        kmer = dna[i : i + k]
        occurrence_dict[kmer] += count_pattern_occurrence(dna, kmer)
    max_freq = max(occurrence_dict.values())
    filtered_dict = {k: v for k, v in occurrence_dict.items() if v == max_freq}

    return filtered_dict


def all_kmers(dna: str, k: int) -> list:
    """ Returns a generator object that produces all kmers in a dna string.
    i.e. all substrings of length k in the dna string.

    doctest: 
    >>> list(all_kmers("abcdefg",3))
    ['abc', 'bcd', 'cde', 'def', 'efg']
    """
    for i in range(len(dna) - k + 1):
        yield dna[i : i + k]


def reverse_complement(dna: str) -> str:
    """ Returns the reverse complement of a dna string.
    
    doctest:
    >>> reverse_complement('GTCA')
    'TGAC'
    """
    swap = dict(zip("ACGT", "TGCA"))
    string = ""
    for char in dna:
        string += swap[char]
    return string[::-1]


def find_pattern_indexes(dna: str, pattern: str) -> list:
    """ Return list of indexes of a overlapping pattern in a string.

    doctest:
    >>> find_pattern_indexes("GATATATGCATATACTT","ATAT")
    [1, 3, 9]
    """
    return [i for i, kmer in enumerate(all_kmers(dna, len(pattern))) if pattern in kmer]


def hamming_distance(a: str, b: str) -> int:
    """ Returns the hamming distance of two strings
    >>> hamming_distance('GGGCCGTTGGT','GGACCGTTGAC')
    3
    """
    if len(a) != len(b):
        raise ValueError("Strings a,b must be of equal length")
    dist = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            dist += 1
    return dist


if __name__ == "__main__":
    import doctest

    doctest.testmod()
