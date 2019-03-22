# -*- coding: utf-8 -*-

import argparse


def init_arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', type=str, default='input.txt')
    parser.add_argument('-o', '--output', type=str, default="out.txt")
    parser.add_argument('-n', '-s', '--size', type=int)
    return parser

