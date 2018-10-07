#!/usr/bin/env python3
import bioutils as b
from typing import Iterable
import random

class Motif:
    def __init__(self, motifs):
        self.motifs = motifs

    def score(self, kmer) -> int:
        score = 0
        for row in self.motifs:
            score += b.hamming_distance(row, kmer)
        return score

    def consensus(self) -> str:
        """ Returns the consensus string of a motif. 
        Consensus_i == Most frequent character in motif.column(i)
        doctest:
        >>> motif = ["ABC","ABC","ABD","AGE"]
        >>> Motif(motif).consensus()
        'ABC'
        """

        out = ""
        for column in zip(*self.motifs):    
            count = b.count_nucleotides(column)
            highest = max(count.values())
            out += {val for val, count in count.items() if count == highest}.pop()
        return out



def random_motifs(dna: Iterable, k: int) -> list:
    """ Returns a list of randomly chosen k-mer inside each dna in the dna iterable """
    random_kmers = []
    n = len(dna[0])
    for string in dna:
        i = random.randint(0, n - k)
        random_kmers.append(string[i : i + k])
    return random_kmers

def greedy_motif_search(dna: list, k: int, pseudo_count: bool = False):
    pass


def randomized_motif_search(dna: list, k: int):
    pass


if __name__ == "__main__":
    import doctest

    doctest.testmod()
