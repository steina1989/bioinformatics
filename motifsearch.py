#!/usr/bin/env python3
import bioutils as b
from typing import Iterable
import random,sys


def greedy_motif_search(dna: list, k: int, pseudo_count: bool = False):

    best_motifs = [kmer[0:k] for kmer in dna]
    t = len(dna)
    
    for kmer in b.iter_substr(dna[0],k):
        motif = [kmer]

        for i in range(1,t):
            profile = b.profile(motif[0:i],False)
            motif.append(b.profile_most_probable_kmer(profile,dna[i],k))
        
        consensus = b.consensus(motif)
        if b.score(motif,consensus) < b.score(best_motifs, consensus):
            best_motifs = motif
    return best_motifs
        



def randomized_motif_search(dna: list, k: int):
    pass


if __name__ == "__main__":

    with open('motif_test.txt') as f:
        k = int(f.readline().strip().split(" ")[0])
        dna = [entry.strip() for entry in f.readlines()]
    greedy_motif_search(dna, k)

