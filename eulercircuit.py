#!/usr/bin/env python3
import collections
import sys
from directedgraph import DirectedGraph


class EulerCircuit(DirectedGraph):
    ''' Class for finding Euler circuit path.
    It is assumed that the provided graph is Eulerian.
    '''

    def __init__(self, line_list):
        super().__init__(line_list)

    def cycle(self):
        pass


if __name__ == "__main__":
    import sys

    with open(sys.argv[1]) as f:
        eu = EulerCircuit(f.readlines())

    eu.cycle()



