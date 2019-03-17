# -*- coding: utf-8 -*-


"""

Реализация 2 задачи через генератор.

"""

import sys
import Task_2_21.utils as tutils
import logic1

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Data file not defined from argv.")
        exit(1)
    # input
    try:
        data = tutils.load_data(sys.argv[1])
    except Exception as e:
        print("Data file load error : " + str(e))
        exit(2)
    # logic

    try:
        result = logic1.find_shape(data)
    except Exception as e:
        print("Data processing error : " + str(e))
        exit(3)

    print(result)
