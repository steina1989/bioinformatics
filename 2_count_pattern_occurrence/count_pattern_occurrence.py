#!/usr/bin/env python3
import sys


def count_pattern_occurrence(dna: str, pattern: str) -> int:
    """ Count pattern occurrence in an arbitrary string, in an overlapping manner.
    >>> count_pattern_occurrence("GCGCG","GCG")
    2
    """

    count = 0
    for i in range(len(dna) - len(pattern) + 1):
        dna_substring = dna[i : i + len(pattern)]
        if pattern in dna_substring:
            count += 1
    return count


if __name__ == "__main__":

    import doctest

    doctest.testmod()

    """ Pipe dataset in via terminal.
    The i/o format conforms to Rosalind's excercise provided i/o format.
    """
    DNA = sys.stdin.readline().strip()
    PATTERN = sys.stdin.readline().strip()
    count = count_pattern_occurrence(DNA, PATTERN)
    print(count)
