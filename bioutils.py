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
    Or more generally, all substrings of length k in a string.

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


def approximate_occurrences(dna: str, pattern: str, d: int) -> list:
    """ Returns list of indeces where there is some k-mer substring pattern that 
    has <= d occurrences of mismatching characters.
    >>> pattern = 'ATTCTGGA'
    >>> dna = 'CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAATGCCTAGCGGCTTGTGGTTTCTCCTACGCTCC'
    >>> approximate_occurrences(dna,pattern,3)
    [6, 7, 26, 27, 78]
    """
    k = len(pattern)
    return [
        i
        for i, kmer in enumerate(all_kmers(dna, k))
        if hamming_distance(kmer, pattern) <= d
    ]


def find_min_skew(dna: str) -> list:
    """ Define skew as the difference between total number of occurrences of G and C.
    Returns indices of all mininum skew locations in a genome.
    """


# 0 -1 -1 -1 0 1 2 1 1 1 0 1 2 1 0 0 0 0 -1 0 -1 -2
#    C  A  T G G G C A T C G G C C A T A  C G  C  C


def find_clumps(dna: str, k: int, L: int, t: int) -> set:
    """ Find distinct k-mers inside a genome forming a (L,t)-clump.
    L length of the clump
    k length of kmer
    t minimal occurrence count of the kmer to give the (L,t)-clump
    doctest:
    >>> dna = 'CGGACTCGACAGATGTGAAGAAATGTGAAGACTGAGTGAAGAGAAGAGGAAACACGACACGACATTGCGACATAATGTACGAATGTAATGTGCCTATGGC'
    >>> sorted(list(find_clumps(dna, 5, 75, 4)))
    ['AATGT', 'CGACA', 'GAAGA']
    """
    out = set()
    # Maybe 'all_kmers' is too narrowly named.
    for substr in all_kmers(dna, L):
        occurrence_dict = collections.defaultdict(int)
        for kmer in all_kmers(substr, k):
            occurrence_dict[kmer] += 1
        out.update([kmer for kmer, count in occurrence_dict.items() if count >= t])

    return out


if __name__ == "__main__":
    import doctest

    doctest.testmod()
