#!/usr/bin/env python3
import sys
from bioutils import reverse_complement

def main(dna):
    print(reverse_complement(dna))
    

if __name__ == "__main__":
    DNA = sys.stdin.readline().strip()
    main(DNA)
