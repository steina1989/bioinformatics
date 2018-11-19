#!/usr/bin/env python3
from collections import defaultdict


class DirectedGraph:
    def __init__(self, string_list):
        self.graph = self.parse(string_list)

    def in_neighbours(self, node):
        return [key for key in self if node in self.graph[key]]

    def out_neighbours(self, node):
        return self.graph[node]

    def __iter__(self):
        return iter(self.graph)

    def __str__(self):
        return "\n".join(
            [
                node
                + " ->"
                + " out: "
                + str(self.out_neighbours(node))
                + " in: "
                + str(self.in_neighbours(node))
                for node in self
            ]
        )

    def parse(self, string_list):
        graph = defaultdict(list)
        for line in string_list:
            node, neighbours = line.strip().split(" -> ")
            graph[node] = neighbours.split(",")
        return graph


if __name__ == "__main__":
    import sys

    with open(sys.argv[1]) as f:
        graph = DirectedGraph(f.readlines())
    print(graph)
