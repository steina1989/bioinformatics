#!/usr/bin/env python3
import sys
import collections

def parse_input(path):
    with open(path) as f:
        return [line.strip() for line in f.readlines()]

def main(kmers):

    bruijn = collections.defaultdict(list)
    k = len(kmers[0])

    for kmer in kmers:
        bruijn[kmer[:-1]].append(kmer[1:])

    out = []

    for key in list(bruijn.keys()):
        out_n = bruijn[key]
        in_n = list_in_neighbours(key, bruijn, k)

        # print(key, "out:", out_n, "in:", in_n)

        if len(in_n) == 1 and len(out_n) == 1:

            new_key = in_n[0] + out_n[0]
            del bruijn
            
        else:
            for outkmer in out_n:
                out.append(key + outkmer[-1])  

    print(*(sorted(out)))


def list_in_neighbours(node, graph, k):

    out = []
    suffix = node[:k-2]

    for prefix in 'ACGT':
        in_node = prefix + suffix
        out_n = graph[in_node]

        for kmer in out_n:
            if kmer in node:
                out.append(in_node)
    return out
    
    
if __name__ == "__main__":
    args = parse_input(sys.argv[1])
    main(args)