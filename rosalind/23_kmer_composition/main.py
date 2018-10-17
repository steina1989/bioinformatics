#!/usr/bin/env python3
import sys
from bioutils import iter_substr


def main(k, dna):
    out = iter_substr(dna, k)
    print("\n".join(out))


if __name__ == "__main__":
    K = int(sys.stdin.readline().strip())
    DNA = sys.stdin.readline().strip()
    main(K, DNA)
