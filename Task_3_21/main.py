# -*- coding: utf-8 -*-



"""

21.	Отрезок на прямой линии задается координатой начала A и координатой окончания B (точки начала и окончания отрезка принадлежат отрезку).
Задан набор отрезков, которые могут накладываться друг на друга. Необходимо выполнить объединение этих отрезков, представив
результат также в виде набора отрезков.
Подсказка: перед объединением необходимо отсортировать отрезки по координате начала отрезка.


"""



# main module
import sys
import utils
import logic

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Data size not defined by argv.")
        exit(1)
    try:
        for i in range(1, int(sys.argv[1]) + 1):
            print("================TEST_{0}================".format(i))
            print("Data load")
            segments = utils.load_data("test_{0}.txt".format(i))
            print("Processing")
            result = logic.get_unions(segments)
            print("Result : ", result)
            print("======================================")
    except Exception as e:
        print("Test failed : " + str(e))
        exit(2)

