#!/usr/bin/env python3

from profile import Profile
import sys


def main(dna, k, profile):
    print(Profile(profile).most_probable_kmer_in_dna(dna, k))


if __name__ == "__main__":
    dna = sys.stdin.readline().strip()
    k = int(sys.stdin.readline().strip())

    profile = [
        list(map(float, entry.strip().split())) for entry in sys.stdin.readlines()
    ]
    main(dna, k, profile)
