# -*- coding: utf-8 -*-

# logic module


def raw(w, h, y, x):
    curx = x
    cury = y
    # top
    distance = w + 1
    while distance > 0:
        yield (cury, curx)
        distance -= 1
        curx += 1
    # right
    distance = h + 1
    while distance > 0:
        yield (cury, curx)
        distance -= 1
        cury += 1
    # bottom
    distance = w + 1
    while distance > 0:
        yield (cury, curx)
        distance -= 1
        curx -= 1
    # left
    distance = h + 1
    while distance > 0:
        yield (cury, curx)
        distance -= 1
        cury -= 1


def isol_circuit(w, h, y, x):
    startx = x - 1
    starty = y - 1
    for point in raw(w, h, starty, startx):
        yield point


def is_shape_exist(y, x, found):
    for shape in found:
        if ((x >= shape[1]) and (x <= shape[1] + shape[3] - 1)) and \
                ((y >= shape[0]) and (y <= shape[0] + shape[2] - 1)):
            return True
    return False


def is_point_in_range(data, y, x):
    return ((x >= 0) and (x < len(data[0]))) and ((y >= 0) and (y < len(data)))


def find_shape(data):
    found_shapes = []
    for y, yv in enumerate(data):
        for x, xv in enumerate(yv):
            # если точка тру и она не часть другой фигуры
            if data[y][x] and (not is_shape_exist(y, x, found_shapes)):
                h = 0
                w = 0
                cury = y
                curx = x
                # прпробуем найти ширину первой строки
                while curx < len(data[y]) and data[cury][curx]:
                    w += 1
                    curx += 1
                # теперь пробуем пройти в глубину, пытаясь найти строки длиной w
                while cury < len(data):
                    curx = x
                    neww = 0
                    while curx < len(data[cury]) and data[cury][curx]:
                        neww += 1
                        curx += 1
                    # если строка такого же размера как эталон, то увеличиваем высоту
                    if neww == w:
                        h += 1
                        cury += 1
                    else:
                        break
                # found_shapes.append([y, x, h, w, h*w])
                # должны найти хотя бы 1 фигуру
                # теперь можно проверить и на изолированность

                is_isol = True
                for point in isol_circuit(w, h, y, x):
                    if not is_point_in_range(data, point[0], point[1]):
                        continue
                    if data[point[0]][point[1]]:
                        is_isol = False
                        break
                if is_isol:
                    found_shapes.append([y, x, w, h, w*h])

    if len(found_shapes) == 0:
        return tuple([-1, -1, -1, -1])
    # после того как нашли все изолированные
    # отберем с макс. площадью
    result = [s for s in found_shapes if s[4] == max(found_shapes, key=lambda sp: sp[4])[4]]
    # отберем верхние
    result = [s for s in result if s[0] == min(result, key=lambda sp: sp[0])[0]]
    # отберем самую левую
    result = [s for s in result if s[1] == min(result, key=lambda sp: sp[1])[1]][0]
    return result
