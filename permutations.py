#!/usr/bin/env python3


class Permutations:
    def __init__(self, input):
        self.permutation = self.__parse__(input)

    def greedy_sort(self):
        self.__reverse__(0, len(self.permutation))
        return self

    def __reverse__(self, a, b):
        reverse = self.permutation[a:b][::-1]
        negate = list(map(lambda x: -x, reverse))
        self.permutation[a:b] = negate

    def __parse__(self, input):
        return list(map(int, input[1:-1].split()))

    def __str__(self):
        return "(" + " ".join(map(self.__i2str__, self.permutation)) + ")"

    def __i2str__(self, i):
        if i > 0:
            return "+" + str(i)
        return str(i)
