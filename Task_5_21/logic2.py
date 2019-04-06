import string

cirillic_upper = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
cirillic_lower = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"


def unique_words_dec(size_filter):
    def unique_internal(*args, **kwargs):
        sized_words = size_filter(*args, **kwargs)
        result = []
        for i in sized_words:
            if i not in result:
                result.append(i)
        return result
    return unique_internal


@unique_words_dec
def select_words(*args, **kwargs):

    if args:
        wordsize = args[0]
        buffer = args[1]
    if kwargs:
        wordsize = kwargs.get('size', None)
        buffer = kwargs.get('data', None)

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

