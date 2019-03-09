# -*- coding: utf-8 -*-

# класс отрезка


class Segment:

    def __init__(self, x1, x2):
        if x2 < x1:
            raise Exception("Invalid segment input")
        self.x1 = x1
        self.x2 = x2

    # для sort
    def __lt__(self, other):
        return (self.x1 <= other.x1) and (self.x2 <= other.x2)

    # segment size
    def __len__(self):
        return self.x2 - self.x1

    # for print()
    def __str__(self):
        # return tuple([self.x1, self.x2])
        return "({0},{1})".format(self.x1, self.x2)

    # for iterable print()
    def __repr__(self):
        # return tuple([self.x1, self.x2])
        return "({0},{1})".format(self.x1, self.x2)

    # for use IN
    def __eq__(self, item):
        return self.x1 == item.x1 and self.x2 == item.x2

    # segments diff
    def __sub__(self, other):
        res = self.x2 - other.x1
        if res < 0:
            return None
        else:
            if res > len(other):
                return Segment(other.x1, other.x1 + res - 1)
            else:
                return Segment(other.x1, other.x1 + res)
