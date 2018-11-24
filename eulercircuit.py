#!/usr/bin/env python3
import collections
import sys


class EulerCircuit:
    def __init__(self, graph, num_edges):
        self.graph = graph
        self.travelled = []
        # ERUm am pæla hvort það sé ekki betra að geyma tvenndir af (frá,til) nóðum sem merkja þá leggina.
        # Hvernig sem það fer, ath að laga is_cycle og unexplored edges dæmið.
        self.num_edges = num_edges

    @classmethod
    def from_file(cls, path):
        num_edges = 0
        graph = collections.defaultdict(list)
        with open(path) as f:
            for line in f.readlines():
                node, out_neighbours = line.strip().split(" -> ")
                for neighbour in out_neighbours.split(","):
                    graph[node].append(neighbour)
                    num_edges += 1
        return cls(graph, num_edges)

    def cycle(self):
        # Bútil hring
        start_node = next(iter(self.graph))

        # Make cycle
        self.traverse(start_node)

        while self.there_are_unexplored_edges():
            # Choose a node in self.travelled that has out neighbour that hasnt been used
            # Transform self.travelled so that it starts at this node from above.
            self.traverse(start_node)

    def traverse(self, node):
        while not self.cycle():
            neighbours = self.graph[node]
            self.travelled.append(neighbours[0])
            node = neighbours[0]

    def there_are_unexplored_edges(self):
        return self.num_edges > len(self.travelled) - 1

    def __str__(self):
        return "->".join(self.travelled)

    def is_cycle(self):
        return self.travelled[0] == self.travelled[-1]


if __name__ == "__main__":
    import sys

    eu = EulerCircuit.from_file(sys.argv[1])

    print(eu.cycle())
