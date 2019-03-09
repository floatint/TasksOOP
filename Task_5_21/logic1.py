# -*- coding: utf-8 -*-

# logic module

import Task_2_21.logic as tlogic


# generator for isolation check

class ShapeFinderEx(tlogic.ShapeFinder):

    def __check_edges(self, y, x, h, w):
        for i in range(x, x + w + 2):
            x = i
            yield (not self._is_point_in_range(y, x)) or (not self._data[y][x])
        for i in range(y, y + h + 2):
            y = i
            yield (not self._is_point_in_range(y, x)) or (not self._data[y][x])
        for i in range(x, x - w - 2, -1):
            x = i
            yield (not self._is_point_in_range(y, x)) or (not self._data[y][x])
        for i in range(y, y - h - 2, -1):
            y = i
            return (not self._is_point_in_range(y, x)) or (not self._data[y][x])

    def __is_shape_isolated(self, shape):
        y = shape[0] - 1
        x = shape[1] - 1
        h = shape[2]
        w = shape[3]
        for r in self.__check_edges(y, x, h, w):
            if not r:
                return False
        return True

    # main override

    def find_shapes(self):
        founded = []
        for y, yv in enumerate(self._data):
            for x, xv in enumerate(yv):
                if xv:
                    new_shape = self._get_shape(y, x, founded)
                    if new_shape is not None:
                        founded.append(new_shape)
        # получим изолированные
        isol_shapes = [iss for iss in founded if self.__is_shape_isolated(iss)]
        if len(isol_shapes) == 0:
            return tuple([-1, -1, -1, -1])
        # если нашли несколько
        # найдем все максимальные
        max_shapes = [s for s in isol_shapes if s[4] == max(isol_shapes, key=lambda sp: sp[4])[4]]
        # из них все верхние
        top_shapes = [s for s in max_shapes if s[0] == min(max_shapes, key=lambda sp: sp[0])[0]]
        # из них самые левый
        left_shape = [s for s in top_shapes if s[1] == min(top_shapes, key=lambda sp: sp[1])[1]][0]
        return tuple(left_shape)

