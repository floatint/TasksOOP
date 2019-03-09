# -*- coding: utf-8 -*-

# logic module


class ShapeFinder:

    # __found_list = []  # фигура = [y, x, h, w, p]

    def __init__(self, dl):
        if len(dl) == 0:
            raise Exception("Data processing error")
        self._data = dl

    @staticmethod
    def __is_shape_exist(y, x, founded):
        for shape in founded:
            if ((x >= shape[1]) and (x <= shape[1] + shape[3] - 1)) and \
                ((y >= shape[0]) and (y <= shape[0] + shape[2] - 1)):
                return True
            else:
                continue
        return False

    def _is_point_in_range(self, y, x):
        return ((x >= 0) and (x < len(self._data[0]))) and ((y >= 0) and (y < len(self._data)))

    """
    def q(self):
        for i in range(x0, x0+width):
            yield (i, y0)
        for i in range(y0, y0+h):
            yield (y0, i)
        for i in range(x0, x0+width):
            yield (i, y0)
        for i in range(x0, x0+width):
            yield (i, y0)"""
    def _is_shape_isolated(self, shape):
        # shape format = [y, x, h, w, p]

        y = shape[0] - 1
        x = shape[1] - 1
        h = shape[2]
        w = shape[3]

        # проверим сверху
        dist = w + 1
        while dist > 0:
            if not self._is_point_in_range(y, x):
                dist -= 1
                x += 1
                continue
            if self._data[y][x]:
                return False
            else:
                dist -= 1
                x += 1
        # проверим право
        dist = h + 1
        while dist > 0:
            if not self._is_point_in_range(y, x):
                dist -= 1
                y += 1
                continue
            if self._data[y][x]:
                return False
            else:
                dist -= 1
                y += 1
        # проверим низ
        dist = w + 1
        while dist > 0:
            if not self._is_point_in_range(y, x):
                dist -= 1
                x -= 1
                continue
            if self._data[y][x]:
                return False
            else:
                dist -= 1
                x -= 1
        # проверим лево
        dist = h + 2
        while dist > 0:
            if not self._is_point_in_range(y, x):
                dist -= 1
                y -= 1
                continue
            if self._data[y][x]:
                return False
            else:
                dist -= 1
                y -= 1
        return True

    def _get_shape(self, y, x, founded):
        # проверим, принадлежит ли (x,y) к найденным фигурам
        # если такой фигуры нет вернем ничего
        if self.__is_shape_exist(y, x, founded):
            return None
        # поиск
        # сторим исходные x, y
        old_x = x
        old_y = y
        # заполняем хар-ки
        p = 0
        w = 0
        h = 0
        # пытаемся пройти в ширину
        t = self._data[y][x]
        o = len(self._data)
        while (x < len(self._data[0])) and (self._data[y][x]):
            w += 1
            x += 1
        # рестор
        x = old_x
        # проход в глубь
        while (y < len(self._data)) and (self._data[y][x]):
            h += 1
            y += 1
        y = old_y
        p = w * h
        return tuple([y, x, h, w, p])

    def find_shapes(self):
        founded = []
        for y, yv in enumerate(self._data):
            for x, xv in enumerate(yv):
                if xv:
                    new_shape = self._get_shape(y, x, founded)
                    if new_shape is not None:
                        founded.append(new_shape)
        # получим изолированные
        isol_shapes = [iss for iss in founded if self._is_shape_isolated(iss)]
        """isol_shapes =[]
        for s in self.__found_list:
            if self.__is_shape_isolated(s):
                isol_shapes.append(s)"""
        if len(isol_shapes) == 0:
            return tuple([-1, -1, -1, -1])
        # если нашли несколько
        # найдем все максимальные
        max_shapes = [s for s in isol_shapes if s[4] == max(isol_shapes, key=lambda sp: sp[4])[4]]
        # из них все верхние
        top_shapes = [s for s in max_shapes if s[0] == min(max_shapes, key=lambda sp: sp[0])[0]]
        # из них самые левый
        left_shape = [s for s in top_shapes if s[1] == min(top_shapes, key=lambda sp: sp[1])[1]][0]
        """max_shape = max(isol_shapes, key=lambda f: f[4])
        max_shapes.append(max_shape)
        isol_shapes.remove(max_shape)
        max_shape = max(isol_shapes, key=lambda f: f[4])
        if max_shape[4] == max_shapes[0][4]:
            max_shapes.append(max_shape)

        if len(max_shapes) == 1:
            return max_shapes

        # вернем сначала верхний а потом левый

        return [min(max_shapes, key=lambda f: f[0]), min(max_shapes, key=lambda f: f[1])]"""
        return tuple(left_shape)
