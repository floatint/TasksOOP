# -*- coding: utf-8 -*-

# класс отрезка


class Segment:

    def __init__(self, x1, x2):
        if x2 < x1:
            raise Exception("Invalid segment input")
        self.x1 = x1
        self.x2 = x2

    # in
    def __contains__(self, other):
        return (self.x1 <= other.x1) and (self.x2 <= other.x2)

    # for iterable print()
    def __repr__(self):
        return "({0},{1})".format(self.x1, self.x2)
