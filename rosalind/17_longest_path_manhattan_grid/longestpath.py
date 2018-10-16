#!/usr/bin/env python3

import io, numpy as np,sys

def main(n, m, down, right):

    x = np.zeros((n,m))


def parse_input(file):
    with open(file) as f:
        n,m = map(int, f.readline().strip().split())
        d = np.loadtxt([f.readline() for _ in range(n)])
        next(f)
        r = np.loadtxt([f.readline() for _ in range(n+1)])
    return n,m,d,r

if __name__ == "__main__":
    input_data = parse_input(sys.argv[1])
    main(*input_data)

    