#!/usr/bin/env python3
import collections
from eulercircuit import EulerCircuit


class EulerPath(EulerCircuit):
    """ What started out as what I thought would be a clever solution
    has become one of my biggest hacks. Please don't, ever, consider
    using this code.
    """

    def __init__(self, graph, num_edges):
        super().__init__(graph, num_edges)
        self.all_keys = set()
        self.get_all_keys()

    def get_all_keys(self):
        for key, neigh_set in self.graph.items():
            self.all_keys.add(key)
            for neigh in neigh_set:
                self.all_keys.add(neigh[0])

    def path(self):
        a, b = self.find_odd_vertices()
        self.graph[b].add((a, False))
        self.cycle()
        self.fix_euler_path(a, b)

    def fix_euler_path(self, a, b):
        travel = self.travelled

        for i in range(len(travel) - 1):
            if travel[i] == b and travel[i + 1] == a:
                self.travelled = travel[i + 1 :] + travel[1:i] + [b]
                return

    def find_odd_vertices(self):
        """ Just look at this atrocity, for the love of ... """
        a = None
        b = None
        for key in self.all_keys:
            out_d = self.out_degree(key)
            in_d = self.in_degree(key)
            if in_d + 1 == out_d:
                a = key
            elif out_d + 1 == in_d:
                b = key
            if a and b:
                return (a, b)

    def out_degree(self, node):
        return len(self.graph[node])

    def in_degree(self, node):
        """ NOOOOO """
        count = 0
        for key in self.graph:
            if (node, False) in self.graph[key]:
                count += 1
        return count


if __name__ == "__main__":
    import sys

    eu = EulerPath.from_file(sys.argv[1])
    eu.path()
    print(eu)
