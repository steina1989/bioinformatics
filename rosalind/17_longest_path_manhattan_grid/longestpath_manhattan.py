#!/usr/bin/env python3

import io, numpy as np, sys


def main(n, m, d, r):

    x = np.zeros((n + 1, m + 1))

    for i in range(n + 1):
        for j in range(m + 1):
            down = value_of(x, d, i - 1, j)
            right = value_of(x, r, i, j - 1)
            x[i, j] = max(down, right)
    return x[n, m]


def value_of(x, edge_matrix, i, j):
    prev_node = 0
    edge = 0
    if i >= 0 and j >= 0:
        prev_node = x[i, j]
        edge = edge_matrix[i, j]
    return prev_node + edge


def parse_input(file):
    with open(file) as f:
        n, m = map(int, f.readline().strip().split())
        d = np.loadtxt([f.readline() for _ in range(n)])
        next(f)
        r = np.loadtxt([f.readline() for _ in range(n + 1)])
    return n, m, d, r


if __name__ == "__main__":
    input_data = parse_input(sys.argv[1])
    res = main(*input_data)
    print(res)
