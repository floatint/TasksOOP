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
    return newlist


def unique_words(size_filter):
    def unique_internal(data, word_size):
        sized_words = size_filter(data, word_size)
        result = []
        for i in range(len(sized_words)):
            if not sized_words[i] in result:
                result.append(sized_words[i])
        return result
    return unique_internal
