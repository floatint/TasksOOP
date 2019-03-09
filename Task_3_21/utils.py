# -*- coding: utf-8 -*-

# support module

import segment


def load_data(filepath):
    f = open(filepath, "rt")
    data = []
    for line in f:
        int_list = [int(x) for x in line.split(" ")]
        if len(int_list) < 2:
            raise Exception("Data currupted.")
        data.append(segment.Segment(int_list[0], int_list[1]))
    f.close()
    return data

