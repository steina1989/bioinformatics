#!/usr/bin/env python3
import sys
from bioutils import count_pattern_occurrence

def main(dna,pattern):
    count = count_pattern_occurrence(dna,pattern)
    print(count)

if __name__ == '__main__':
    DNA = sys.stdin.readline().strip()
    PATTERN = sys.stdin.readline().strip()

    main(DNA, PATTERN)