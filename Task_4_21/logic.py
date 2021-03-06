# -*- coding: utf-8 -*-

# logic module

import string

cirillic_upper = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
cirillic_lower = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

def select_words(buffer, wordsize):
    tmp = ''
    newlist = []
    for c in buffer:
        if c not in string.ascii_uppercase:
            if c not in string.ascii_lowercase:
                if c not in cirillic_upper:
                    if c not in cirillic_lower:
                        if c not in string.digits:
                            if len(tmp) == wordsize:
                                newlist.append(tmp)
                            tmp = ''
                            continue
        tmp += c
    return list(set(newlist))
