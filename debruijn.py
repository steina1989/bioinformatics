#!/usr/bin/env python3
import collections


class DeBruijn:
    def __init__(self, path):
        self.bruijn = self.construct_debruijn(path)

    def construct_debruijn(self, path):
        bruijn = collections.defaultdict(list)

        with open(path) as f:
            for line in f.readlines():
                kmer = line.strip()
                bruijn[kmer[:-1]].append(kmer[1:])

        return bruijn

    def contigs(self):
        contigs = []
        chains = self._all_chains()

        for node in list(self.bruijn.keys()):
            if node in chains:
                continue
            contigs += self.glue(node)
        return contigs

    def glue(self, node):
        out = []
        for neighbour in self.out_neighbours(node):
            str_build = node
            while self._is_subchain(neighbour):
                str_build += neighbour[-1]
                neighbour = self.out_neighbours(neighbour)[0]
            str_build += neighbour[-1]
            out.append(str_build)

        return out

    def _is_subchain(self, node):
        return (
            len(self.in_neighbours(node)) == 1 and len(self.out_neighbours(node)) == 1
        )

    def _all_chains(self):
        out = set()
        for node in list(self.bruijn.keys()):
            if self._is_subchain(node):
                out.add(node)
        return out

    def in_neighbours(self, node):

        out = []
        suffix = node[:-1]

        for prefix in "ACGT":
            in_node = prefix + suffix
            out_n = self.bruijn[in_node]

            for kmer in out_n:
                if kmer in node:
                    out.append(in_node)
        return out

    def out_neighbours(self, node):
        return self.bruijn[node]


if __name__ == "__main__":
    import sys

    bla = DeBruijn(sys.argv[1])

    print(*sorted(bla.contigs()))
