#!/usr/bin/env python3
import sys
import collections


def parse_input(path):
    with open(path) as f:
        return [line.strip() for line in f.readlines()]


def main(kmers):

    bruijn = collections.defaultdict(list)

    for kmer in kmers:
        bruijn[kmer[:-1]].append(kmer[1:])

    for key, val in sorted(bruijn.items()):
        print(key, "->", ",".join(val))


if __name__ == "__main__":
    args = parse_input(sys.argv[1])
    main(args)
