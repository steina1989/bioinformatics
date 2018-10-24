#!/usr/bin/env python3
import sys
from bioutils import de_bruijn_from_string


def main(dna, k):
    graph = de_bruijn_from_string(dna, k)
    for key, val in sorted(graph.items()):
        print(key, "->", ",".join(sorted(val)))


if __name__ == "__main__":
    K = int(sys.stdin.readline().strip())
    DNA = sys.stdin.readline().strip()
    main(DNA, K)
