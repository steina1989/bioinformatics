import bioutils as b

class MotifSearch:

    def __init__(self):
        pass
        

class Motif:
    
    def __init__(self, motifs):
        self.motifs = motifs

    def score(self) -> int:
        pass

    def consensus(self) -> str:
        """
        test...
        >>>  1 == 2
        True
        """

        for column in zip(*self.motifs): 
            count = b.count_nucleotides(column)
            print(count)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
