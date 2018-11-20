#!/usr/bin/env python3


class Permutations:
    def __init__(self, input):
        self.permutation = self.__parse(input)

    def greedy_sort(self):
        for i in range(len(self.permutation)):
            sorted_val = i + 1
            if self.permutation[i] != sorted_val:
                index = self.__find_index(sorted_val)
                self.__reverse(i,index)
            if self.permutation[i] < 0:
                self.__reverse(i,i)
    
    def __find_index(self, val):
        for i, item in enumerate(self.permutation):
            if val == item or val == -item:
                return i

    def __reverse(self, a, b):
        reverse = self.permutation[a:b+1][::-1]
        negate = list(map(lambda x: -x, reverse))
        self.permutation[a:b+1] = negate
        print(self)

    def __parse(self, inp):
        return list(map(int, inp[1:-1].split()))

    def __str__(self):
        return "(" + " ".join(map(self.__i2str, self.permutation)) + ")"

    def __i2str(self, i):
        if i > 0:
            return "+" + str(i)
        return str(i)


if __name__ == "__main__":
    import sys
    with open(sys.argv[1]) as f:
        perm = Permutations(f.readline().strip())

    perm.greedy_sort()


