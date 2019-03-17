# -*- coding: utf-8 -*-



"""


1.	(*) Для переданного двумерного массива логических элементов, найти наибольший по площади прямоугольник, который полностью состоит из истинных значений,
окруженный ложными значениями или границами массива.
Если существует несколько таких прямоугольников максимальной площади, вернуть самый верхний (по верхнему левому углу), затем самый левый.
На картинках ниже обведены такие прямоугольники для входного массива (закрашенные клетки – истина, белые – ложь):

Функция поиска должна вернуть координату верхнего левого угла прямоугольника и высоту + ширину (для приведенных картинок это будет (1, 6, 3, 2) и (4, 1, 1, 7)).
Если прямоугольник по условиям задачи найти не удалось, то функция должна вернуть (-1, -1, -1, -1).


"""

# main module
import sys
import utils
import logic

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Data file not defined from argv.")
        exit(1)
    # input
    try:
        data = utils.load_data(sys.argv[1])
    except Exception as e:
        print("Data file load error : " + str(e))
        exit(2)
    # logic

    try:
        shape = logic.find_shape(data)
    except Exception as e:
        print("Data processing error : " + str(e))
        exit(3)

    print(shape)




