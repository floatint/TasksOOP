# -*- coding: utf-8 -*-

# logic module

import string

cirillic_upper = "А,Б,В,Г,Д,Е,Ё,Ж,З,И,Й,К,Л,М,Н,О,П,Р,С,Т,У,Ф,Х,Ц,Ч,Ш,Щ,Ъ,Ы,Ь,Э,Ю,Я".split(",")
cirillic_lower = "а,б,в,г,д,е,ё,ж,з,и,й,к,л,м,н,о,п,р,с,т,у,ф,х,ц,ч,ш,щ,ъ,ы,ь,э,ю,я".split(",")

def select_words(buffer, wordsize):
    tmp = ''
    newList = []
    for c in buffer:
        if c not in string.ascii_uppercase:
            if c not in string.ascii_lowercase:
                if c not in cirillic_upper:
                    if c not in cirillic_lower:
                        if c not in string.digits:
                            if len(tmp) == wordsize:
                                newList.append(tmp)
                            tmp = ''
                            continue
        tmp += c
    return list(set(newList))
