# -*- coding: utf-8 -*-

"""

21.	Выбрать (в виде списка) без повторений из текста все слова заданной длины. Словом считается непрерывная последовательность
символов (строчных и прописных) А-Я, A-Z и цифр.

"""



import sys
import logic
import utils

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Data file not defined by argv.")
        exit(1)
    word_size = int(input("Enter word size :"))

    try:
        words = utils.load_data(sys.argv[1])
    except Exception as e:
        print("Data load error : " + str(e))
        exit(2)

    if word_size < 1:
        print("Invalid word size parameter")
        exit(3)

    try:
        processed = logic.select_words(words, word_size)
    except Exception as e:
        print("Data processing error : " + str(e))
        exit(4)

    if len(processed) == 0:
        print("Not found")
        exit(5)
    print(processed)


