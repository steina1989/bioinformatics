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

    for key in list(bruijn.keys()):
        out_n = bruijn[key]
        in_n = list_in_neighbours(key, bruijn)

        if not ( len(in_n) == 1 and len(out_n) == 1 ) : 
            pass


        else:
            in_neighbour = in_n[0]
            out_neighbour = out_n[0]

            index = bruijn[in_neighbour].index(key)
            bruijn[in_neighbour][index] = key[0] + out_neighbour
            del bruijn[key]

    out = []
    for node, val in bruijn.items():
        for neighbour in val:
            out.append(node[0] + neighbour)

    print(*(sorted(out)))


def list_in_neighbours(node, graph):

    out = []
    suffix = node[:-1]

    for prefix in "ACGT":
        in_node = prefix + suffix
        out_n = graph[in_node]

        for kmer in out_n:
            if kmer in node:
                out.append(in_node)
    return out


if __name__ == "__main__":
    args = parse_input(sys.argv[1])
    main(args)
