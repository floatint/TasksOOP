# -*- coding: utf-8 -*-

# support module


def load_data(filepath):
    f = open(filepath, "rt")
    data = f.read()
    # for line in f:
    #     data = line.split(" ")
    f.close()
    return data


def save_data(filepath, data):
    f = open(filepath, "w+")
    for i in data:
        f.write(i)
        f.write('\n')
    f.close()
