# -*- coding: utf-8 -*-

# logic module

import string

cirillic_alphabet = "А,Б,В,Г,Д,Е,Ё,Ж,З,И,Й,К,Л,М,Н,О,П,Р,С,Т,У,Ф,Х,Ц,Ч,Ш,Щ,Ъ,Ы,Ь,Э,Ю,Я".split(",")


def word_valid(word):
    for c in word:
        if c not in cirillic_alphabet:
            if c not in string.ascii_uppercase:
                if c not in string.digits:
                    return False
    return True


def select_words(words, wordsize):
    return list(set(filter(lambda x: word_valid(x) and len(x) == wordsize, words)))
