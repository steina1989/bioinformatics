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


if __name__ == "__main__":

    with open(sys.argv[1]) as f:
        k = int(f.readline().strip().split(" ")[0])
        dna = [entry.strip() for entry in f.readlines()]
    res = greedy_motif_search(dna, k, False)
    print("\n".join(res))
