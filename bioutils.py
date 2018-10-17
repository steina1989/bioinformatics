#!/usr/bin/env python3
import collections
import itertools as it
import numpy as np
from typing import Iterable


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
    for kmer in iter_substr(dna, k):
        if pattern in kmer:
            count += 1
    return count


def most_frequent_kmer(dna: str, k: int) -> set:
    """Returns a set of the most frequent k-mers in a dna string.
    
    doctest:
    >>> sorted(most_frequent_kmer("ACGTTGCATGTCGCATGATGCATGAGAGCT",4))
    ['CATG', 'GCAT']
    """
    occurrence_dict = collections.defaultdict(int)
    for kmer in iter_substr(dna, k):
        occurrence_dict[kmer] += count_pattern_occurrence(dna, kmer)
    max_freq = max(occurrence_dict.values())
    return {kmer for kmer, c in occurrence_dict.items() if c == max_freq}


def most_frequent_approx_kmer(dna: str, k: int, d: int) -> set:
    """ Returns the set of the most frequent approximate kmers in a dna string that
    have a hamming distance of at most d from any kmer in the dna.
    doctest:
    >>> dna = 'ACGTTGCATGTCGCATGATGCATGAGAGCT'
    >>> sorted(most_frequent_approx_kmer(dna,4,1))
    ['ATGC', 'ATGT', 'GATG']
    """
    occurrence_dict = collections.defaultdict(int)
    for kmer in iter_substr(dna, k):
        for product in it.product("ACGT", repeat=k):
            dist = hamming_distance(kmer, product)
            if dist <= d:
                occurrence_dict["".join(product)] += 1

    max_freq = max(occurrence_dict.values())
    return {kmer for kmer, count in occurrence_dict.items() if count == max_freq}


def motif_enumeration(dna: Iterable, k: int, d: int) -> set:
    """ Finds and returns all (k,d)-motifs in a collection of strings.
    Given a collection of strings Dna and an integer d, a k-mer is a (k,d)-motif if it
    appears in every string from Dna with at most d mismatches.
    doctest:
    >>> dna = ['ATTTGGC','TGCCTTA','CGGTATC','GAAAATT']
    >>> sorted(motif_enumeration(dna,3,1))
    ['ATA', 'ATT', 'GTT', 'TTT']
    """
    kmer_sets = []

    for line in dna:
        line_set = set()
        for kmer in iter_substr(line, k):
            for product in it.product("ACGT", repeat=k):
                dist = hamming_distance(kmer, product)
                if dist <= d:
                    line_set.add("".join(product))
        kmer_sets.append(line_set)
    return set.intersection(*kmer_sets)


def hamming_distance(a: str, b: str) -> int:
    """ Returns the hamming distance of two strings

    doctest:
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


def minimal_hamming_dist(pattern: str, text: str) -> int:
    """ Returns the lowest distance a pattern of length k has for all k-mers in text.
    A.k.a. d(Pattern, Text)

    doctest:
    >>> minimal_hamming_dist("BB", "AAAAAAABAAAA")
    1
    """
    lowest = float("inf")
    for kmer in iter_substr(text, len(pattern)):
        dist = hamming_distance(kmer, pattern)
        lowest = min(dist, lowest)
    return lowest


def minimal_hamming_dist_sum(pattern: str, dna: list) -> int:
    """ Returns the 
    A.k.a. d(Pattern, Dna)
    """
    return sum(minimal_hamming_dist(pattern, dna) for dna in dna)


def median_string(dna: Iterable, k: int) -> str:
    """ 
    >>> a = ['AAATTGACGCAT','GACGACCACGTT','CGTCAGCGCCTG','GCTGAGCACCGG','AGTACGGGACAG']
    >>> median_string(a, 3)
    'ACG'
    """
    dist = float("inf")
    median = ""
    for product in it.product("ACGT", repeat=k):
        pattern = "".join(product)
        new_dist = minimal_hamming_dist_sum(pattern, dna)
        if new_dist < dist:
            dist = new_dist
            median = pattern
    return median


def iter_substr(dna: str, k: int):
    """ Returns a generator that produces all kmers in a dna string.
    Or more generally, all substrings of length k in a string.

    doctest: 
    >>> list(iter_substr("abcdefg",3))
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
    return [
        i for i, kmer in enumerate(iter_substr(dna, len(pattern))) if pattern in kmer
    ]


def approximate_occurrences(dna: str, pattern: str, d: int) -> list:
    """ Returns list of indeces where there is some k-mer substring pattern that 
    has <= d occurrences of mismatching characters.

    doctest:
    >>> pattern = 'ATTCTGGA'
    >>> dna = 'CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAATGCCTAGCGGCTTGTGGTTTCTCCTACGCTCC'
    >>> approximate_occurrences(dna,pattern,3)
    [6, 7, 26, 27, 78]
    """
    k = len(pattern)
    return [
        i
        for i, kmer in enumerate(iter_substr(dna, k))
        if hamming_distance(kmer, pattern) <= d
    ]


def find_min_skew(dna: str) -> list:
    """ Define skew as the difference between total number of occurrences of G and C.
    Returns indices of all mininum skew locations in a genome.

    doctest:
    >>> dna = 'CCTATCGGTGGATTAGCATGTCCCTGTACGTTTCGCCGCGAACTAGTTCACACGGCTTGATGGCAAATGGTTTTTCCGGCGACCGTAATCGTCCACCGAG'
    >>> find_min_skew(dna)
    [53, 97]
    """
    current_count = 0
    list_counts = [current_count]
    for char in dna:
        if "C" in char:
            current_count -= 1
        elif "G" in char:
            current_count += 1
        list_counts.append(current_count)

    minimum = min(list_counts)
    return [i for i, val in enumerate(list_counts) if val == minimum]


def find_clumps(dna: str, k: int, L: int, t: int) -> set:
    """ Find distinct k-mers inside a genome forming a (L,t)-clump.
    L length of the clump
    k length of kmer
    t minimal occurrence count of the kmer to give the (L,t)-clump

    doctest:
    >>> dna = 'CGGACTCGACAGATGTGAAGAAATGTGAAGACTGAGTGAAGAGAAGAGGAAACACGACACGACATTGCGACATAATGTACGAATGTAATGTGCCTATGGC'
    >>> sorted(find_clumps(dna, 5, 75, 4))
    ['AATGT', 'CGACA', 'GAAGA']
    """
    out = set()
    for substr in iter_substr(dna, L):
        occurrence_dict = collections.defaultdict(int)
        for kmer in iter_substr(substr, k):
            occurrence_dict[kmer] += 1
        out.update([kmer for kmer, count in occurrence_dict.items() if count >= t])

    return out


def profile(motif: list, pseudo_count: bool = True) -> list:
    """ Returns the profile of a given motif. Setting pseudo_count to true will increment each
    occurrence count of a base by one.
    """
    base_to_index = dict(zip("ACGT", range(4)))
    out = [[], [], [], []]
    incr = 0
    if pseudo_count:
        incr = 1

    length = len(motif)
    for column in zip(*motif):
        count = count_nucleotides(column)
        for base in "ACGT":
            index = base_to_index[base]
            out[index].append(count[base] / length + incr)
    return out


def score(motif: list, consensus: str) -> int:
    """ Returns the score of a given motif. It is the sum aggregate of the hamming distances of each row in the 
    consensus list and the consensus string for the motif. You need to calculate a consensus string seperately beforehand.
    """
    score = 0
    for row in motif:
        score += hamming_distance(row, consensus)
    return score


def consensus(motif: list) -> str:
    """ Returns one consensus string of a motif (there may be more than one)
    Consensus_i == Most frequent character in motif.column(i)
    doctest:
    >>> motif = ["ABC","ABC","ABD","AGE"]
    >>> consensus(motif)
    'ABC'
    """

    out = ""
    for column in zip(*motif):
        count = count_nucleotides(column)
        highest = max(count.values())
        out += {val for val, count in count.items() if count == highest}.pop()
    return out


def probability_of_kmer(profile: list, kmer: str) -> float:
    """ Returns the probability that a single kmer was generated by a given profile matrix. """

    base_to_index = dict(zip("ACGT", range(4)))
    odds = 1.0
    for i, base in enumerate(kmer):
        index = base_to_index[base]
        odds *= profile[index][i]
    return odds


def profile_most_probable_kmer(profile: list, dna: str, k: int):
    """ Returns that kmer in dna that has the highest chance of having been 
    generated by the profile. In case of multiple kmers having equal highest change,
    return the one occurring first."""

    highest_odds = 0
    most_probable = ""
    for kmer in iter_substr(dna, k):
        odds = probability_of_kmer(profile, kmer)
        if odds > highest_odds:
            highest_odds = odds
            most_probable = kmer
    return most_probable



if __name__ == "__main__":
    import doctest

    doctest.testmod()
