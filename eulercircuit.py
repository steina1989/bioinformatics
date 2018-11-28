#!/usr/bin/env python3
import collections
import sys

class EulerCircuit:
    def __init__(self, graph, num_edges):
        self.graph = graph
        self.travelled = []
        self.num_edges = num_edges

    @classmethod
    def from_file(cls, path):
        num_edges = 0
        graph = collections.defaultdict(set)
        with open(path) as f:
            for line in f.readlines():
                node, out_neighbours = line.strip().split(" -> ")
                for neighbour in out_neighbours.split(","):
                    graph[node].add((neighbour, False))
                    num_edges += 1
        return cls(graph, num_edges)

    def cycle(self):

        start_node = next(iter(self.graph))
        self.traverse(start_node)
        while self.there_are_unexplored_edges():

            node = self.find_new_start()
            self.fix_travelled(node)

            self.traverse(node)

    def traverse(self, node):

        while True:
            self.travelled.append(node)
            set_neighbours = self.graph[node]
            neighbour = self.find_untravelled(set_neighbours)
            if not neighbour:
                break
            self.mark_travelled(node,neighbour)
            node = neighbour[0]

    def fix_travelled(self,node):
        out = self.travelled

        out = out[0:-1]
        index = out.index(node)
        self.travelled = out[index:] + out[0:index] 

    def find_new_start(self):
        for key in (set(self.travelled)):
            if self.find_untravelled(self.graph[key]):
                return key


    def find_untravelled(self, set_neighbours):
        for neighbour in set_neighbours:
            if not neighbour[1]:
                return neighbour
        return None

    def mark_travelled(self, node, neighbour):
        self.graph[node].remove((neighbour[0], False))
        self.graph[node].add((neighbour[0], True))

    def there_are_unexplored_edges(self):
        return self.num_edges > len(self.travelled) - 1

    def __str__(self):
        return "->".join(self.travelled)

    def debug_print(self):
        for x, y in self.graph.items():
            print(x, y)


if __name__ == "__main__":
    import sys

    eu = None
    if len(sys.argv) == 1:
        eu = EulerCircuit.from_file('rosalind/27_eulerian_cycle/test.txt')
    else:
        eu = EulerCircuit.from_file(sys.argv[1])
    eu.cycle()
    print(eu)