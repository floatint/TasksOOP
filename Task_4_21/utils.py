# -*- coding: utf-8 -*-

# support module


def load_data(filepath):
    f = open(filepath, "rt")
    data = []
    for line in f:
        data = line.split(" ")
    f.close()
    return data
