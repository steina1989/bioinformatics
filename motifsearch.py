#!/usr/bin/env python3
import bioutils as b
import random, sys


def greedy_motif_search(dna: list, k: int, pseudo: bool):

    best_motifs = [kmer[0:k] for kmer in dna]

    t = len(dna)

    for kmer in b.iter_substr(dna[0], k):
        motif = [kmer]

        for i in range(1, t):
            profile = b.profile(motif[0:i], pseudo)
            most_probable = b.profile_most_probable_kmer(profile, dna[i], k)
            motif.append(most_probable)

        if b.score(motif) < b.score(best_motifs):
            best_motifs = motif
    return best_motifs

def randomized_motif_search(dna,k):
    best_motifs = _randomized_motif_search(dna,k)
    for _ in range(1001):
        motifs = _randomized_motif_search(dna,k)
        if b.score(motifs) < b.score(best_motifs):
            best_motifs = motifs
    return best_motifs

def _randomized_motif_search(dna, k):

    # Randomly select kmers Motifs in each string
    motifs = []
    for string in dna:
        r = random.randint(0,len(string)-k)
        motifs.append(string[r:r+k])
    best_motifs = motifs

    while True:
        profile = b.profile(motifs, True)
        motifs = _motifs(profile, dna,k)
        if b.score(motifs) < b.score(best_motifs):
            best_motifs = motifs
        else:
            return best_motifs


def _motifs(profile, dna,k):
    motifs = []
    for sequence in dna:
        motifs.append(b.profile_most_probable_kmer(profile, sequence,k))
    return motifs

if __name__ == "__main__":
    import sys
    with open(sys.argv[1]) as f:
        k = int(f.readline().strip().split(" ")[0])
        dna = [entry.strip() for entry in f.readlines()]
    res = randomized_motif_search(dna, k)
    print("\n".join(res))
