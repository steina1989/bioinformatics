#!/usr/bin/env python3
import sys
import collections


def count_nucleotides(dna: str) -> collections.defaultdict:
    """ Counts character occurrence in arbitrary string, aptly named due to
    context of this course.
    >>> sorted(count_nucleotides("GCTCA").items())
    [('A', 1), ('C', 2), ('G', 1), ('T', 1)]
    """
    occurrence_dict = collections.defaultdict(int)
    for char in dna:
        occurrence_dict[char] += 1
    return occurrence_dict


if __name__ == "__main__":

    import doctest

    doctest.testmod()

    """ Pipe dataset in via terminal.
    The i/o format conforms to Rosalind's excercise provided i/o format.
    """
    data = sys.stdin.readline().strip()
    dna = count_nucleotides(data)
    print(dna["A"], dna["C"], dna["G"], dna["T"])
