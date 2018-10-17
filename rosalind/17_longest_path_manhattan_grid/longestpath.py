#!/usr/bin/env python3

import io, numpy as np,sys

def main(n, m, d, r):

    x = np.zeros((n+1,m+1))

    for i in range(n+1):
        for j in range(m+1):
            down = from_above(x,d,i,j)
            right = from_left(x,r,i,j)

            x[i,j] = max(down,right)
    
    print(x)
    return x[n,m]

def from_above(x,down,i,j):
    prev_node = 0
    upper = 0
    if i-1 >= 0:
        prev_node = x[i-1,j]
        upper = down[i,j]
    return prev_node + upper

def from_left(x,right,i,j):
    prev_node = 0
    rightnumber = 0
    if j-1 >= 0:
        prev_node = x[i,j-1]
        rightnumber = right[i,j]
    return prev_node + rightnumber


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

