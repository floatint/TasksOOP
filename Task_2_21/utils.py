# -*- coding: utf-8 -*-

# support module


def load_data(filepath):
    f = open(filepath, "rt", newline="\r\n")
    data = []
    for line in f:
        # int_list = [int(x) for x in line.split(" ")]
        data.append([bool(x) for x in [int(y) for y in line.split(" ")]])
    f.close()
    return data
