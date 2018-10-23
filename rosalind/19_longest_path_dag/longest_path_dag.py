#!/usr/bin/env python3

from collections import defaultdict
import sys


def parse_input(file_path):
    with open(file_path) as f:
        source = f.readline().strip()
        sink = f.readline().strip()
        graph = defaultdict(list)
        for line in f.readlines():
            a, b, dist = line.strip().replace("->", ":").split(":")
            graph[a].append((b, int(dist)))
    return source, sink, graph


def main(source, sink, graph):
    a = graph["24"]
    print(a)


if __name__ == "__main__":
    input_data = parse_input(sys.argv[1])

    main(*input_data)
