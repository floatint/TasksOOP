# -*- coding: utf-8 -*-

# input module


def splitnumbers(delimiter, str):
    newlist = []
    tmp = ''

    for c in str:
        if c == delimiter:
            if len(tmp) == 0:
                continue
            else:
                newlist.append(int(tmp))
                tmp = ''
        else:
            tmp += c
    """for i, c in enumerate(str):
        if str[i] == delimiter:
            if len(tmp) == 0:
                continue
            else:
                newlist.append(int(tmp))
                tmp = ''
        else:
            tmp += c"""
    if len(tmp) != 0:
        newlist.append(int(tmp))
        tmp = ''

    if len(newlist) == 0:
        return None
    else:
        return newlist


def loadfromfile(filepath):
    file = open(filepath, 'rt')
    buff = file.readline()
    nums1 = splitnumbers(' ', buff)
    buff = file.readline()
    nums2 = splitnumbers(' ', buff)
    return nums1, nums2


def getfrominput():
    ok = True
    newlist = []
    while ok:
        x = input("Enter the element (~ for end of input) : ")
        if x == "~":
            ok = False
        else:
            newlist.append(int(x))
    if len(newlist) == 0:
        return None
    else:
        return newlist
