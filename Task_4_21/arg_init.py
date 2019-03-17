# -*- coding: utf-8 -*-

import argparse


def init_arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-in', type=str, default='input.txt')
    parser.add_argument('-out', type=str, default="out.txt")
    return parser

