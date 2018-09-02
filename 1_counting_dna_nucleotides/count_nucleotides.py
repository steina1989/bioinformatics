#!/usr/bin/env python3
import sys
import collections


def count_nucleotides(dna: str) -> collections.defaultdict:
    """ Counts character occurrence in arbitrary string, aptly named in the
    context of this course. """
    occurrence_dict = collections.defaultdict(int)
    for char in dna:
        occurrence_dict[char] += 1
    return occurrence_dict


if __name__ == '__main__':
    """ Pipe dataset in via terminal.
    The i/o format conforms to Rosalind's excercise provided i/o format.
    """
    data = sys.stdin.readline().strip()
    dna = count_nucleotides(data)
    print(dna['A'], dna['C'], dna['G'], dna['T'])
