#!/usr/bin/env python3


class Dur:
    def bla(self):
        print("foo")

    @classmethod
    def dur_from_something(cls):
        # semi flott
        # return Dur()
        # enn flottara
        return cls()

    def __str__(self):
        return "foo"

    def __foo(self):
        return "lba"


if __name__ == "__main__":
    a = Dur()
