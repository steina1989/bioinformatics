#!/usr/bin/env python3
import sys
from bioutils import reconstruct_string


def main(kmers):
    print(reconstruct_string(kmers))

if __name__ == "__main__":
    kmers = [line.strip() for line in sys.stdin.readlines()]
    main(kmers)
