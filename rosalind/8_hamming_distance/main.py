#!/usr/bin/env python3
import sys
from bioutils import hamming_distance


def main(a, b):
    print(hamming_distance(a, b))


if __name__ == "__main__":
    A = sys.stdin.readline().strip()
    B = sys.stdin.readline().strip()
    main(A, B)
