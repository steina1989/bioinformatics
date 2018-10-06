#!/usr/bin/env python3
import sys
from bioutils import median_string


def main(dna, k):
    print(median_string(dna, k))


if __name__ == "__main__":
    K = int(sys.stdin.readline().strip())
    DNA = [entry.strip() for entry in sys.stdin.readlines()]
    main(DNA, K)
