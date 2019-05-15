import Task_6_21.game.utils as utils
import Task_6_21.game.seqformatter as sf
import Task_6_21.game.logic_support as ls
import random
import copy
from enum import Enum


# направления шагов
class ShiftDirection(Enum):
    UP = 0,
    DOWN = 1,
    LEFT = 2,
    RIGHT = 3


class Game:

    # Размер игрового поля
    @property
    def size(self):
        return dict({'width': self.__w, 'height': self.__h})

    # Возможные значения для итемов
    @staticmethod
    def item_values():
        return [0, 1, 2]

    # Возвращает возможные шаги
    @property
    def steps(self):
        return self.__sequences

    # Уровень закончен ?
    @property
    def is_complete(self):
        # посчитаем кол-во доступных итемов
        avail_cnt = 0
        for y in range(self.__h):
            for x in range(self.__w):
                if self.__field[y][x].is_available:
                    avail_cnt += 1
        # посчитаем кол-во удаленных
        del_cnt = 0
        for y in range(self.__h):
            for x in range(self.__w):
                if self.__field[y][x].is_deleted:
                    del_cnt += 1
        if del_cnt == avail_cnt:
            return True
        return False

    # Init
    def __init__(self, levelpath):
        self.__field = utils.load_level(levelpath)
        self.__new_field = None
        self.__h = len(self.__field)
        self.__w = len(self.__field[0])
        self.__fill_field(self.__field)
        self.__sequences = None

    # Возвращает ячейку
    def item(self, y, x):
        if self.__new_field:
            return self.__new_field[y][x]
        else:
            return self.__field[y][x]

    # Рандомное заполнение
    @staticmethod
    def __fill_field(field):
        # возможные значеия итемов
        for y in range(len(field)):
            for x in range(len(field[0])):
                field[y][x].value = random.choice(Game.item_values())
        # получим список готовых последовательностей


        seqs = []
        # по строкам
        [seqs.append(i) for i in Game.find_seqs(field, sf.RowSequenceFmt)]
        # по столбцам
        [seqs.append(i) for i in Game.find_seqs(list(zip(*field)), sf.ColSequenceFmt)]
        # anti-random
        while len(seqs) != 0:
            for i in seqs:
                if i[3] == 0:
                    for v in range(i[1]+i[2]):
                        field[i[0]][v].value = random.choice(Game.item_values())
                if i[3] == 1:
                    for v in range(i[0] + i[2]):
                        field[v][i[1]].value = random.choice(Game.item_values())
            seqs.clear()
            # по строкам
            [seqs.append(i) for i in Game.find_seqs(field, sf.RowSequenceFmt)]
            # по столбцам
            [seqs.append(i) for i in Game.find_seqs(list(zip(*field)), sf.ColSequenceFmt)]

    # release version
    # Возвращает последовательность, котрую можно удалить
    # seq = (y,x,size, direction)
    # SequenceFormatter определяет как расположена последовательность
    @staticmethod
    def find_seqs(field, fmt: sf.SequenceFormatter):
        # по строкам
        for y in range(len(field)):
            curstep = []
            for x in range(len(field[0])):
                if not field[y][x].is_available:
                    if len(curstep) >= 3:
                        yield fmt.format(y, x, len(curstep))
                    curstep.clear()
                    continue
                if len(curstep) == 0:
                    curstep.append(field[y][x].value)
                else:
                    if curstep[0] == field[y][x].value:
                        curstep.append(field[y][x].value)
                    else:
                        if len(curstep) >= 3:
                            yield fmt.format(y, x, len(curstep))
                        curstep.clear()
                        curstep.append(field[y][x].value)
            if len(curstep) >= 3:
                yield fmt.format(y, len(field[0]), len(curstep))

    # тоже, что и вверху, только чуть-чуть подредачить
    @staticmethod
    def fnd_seq(field, fmt: sf.SequenceFormatter):
        size = 0
        # проход по строкам
        for y in range(len(field)):
            civ = field[y][0].value
            for x in range(len(field[0])):
                if not field[y][x].is_available:
                    if size >= 3:
                        yield fmt.format(y, x, size)
                    size = 0
                else:
                    if civ == field[y][x].value:
                        size += 1
                    else:
                        civ = field[y][x].value
                        if size >= 3:
                            yield fmt.format(y, x, size)
                        size = 1
            if size >= 3:
                yield fmt.format(y, x, size)
            size = 0

    # Сдвиг строки
    def row_shift(self, y, x, sd: ShiftDirection):
        # копия матрицы
        if self.__new_field:
            newfield = self.__new_field
        else:
            newfield = copy.deepcopy(self.__field)

        row = ls.get_available_row(newfield, y, x)
        if not row:
            return

        # двигаем согласно sd
        if sd == ShiftDirection.LEFT:
            # сохраняем 1 элемент
            i = newfield[y][row[0]].value
            for x in range(row[0], row[1]):
                newfield[y][x].value = newfield[y][x + 1].value
            newfield[y][row[1]].value = i
        if sd == ShiftDirection.RIGHT:
            # сохраняем последний элемент
            i = newfield[y][row[1]].value
            for x in range(row[1], row[0], -1):
                try:
                    newfield[y][x].value = newfield[y][x - 1].value
                except Exception as ex:
                    print(str(ex))
            newfield[y][row[0]].value = i


        self.__sequences = []
        # Найдем возможные ходы
        [self.__sequences.append(i) for i in Game.find_seqs(newfield, sf.RowSequenceFmt)]
        [self.__sequences.append(i) for i in Game.find_seqs(list(zip(*newfield)), sf.ColSequenceFmt)]

        # заполним изменившуюся матрицу
        self.__new_field = newfield

    # сдвиг столбца
    def col_shift(self, y, x, sd: ShiftDirection):
        if self.__new_field:
            newfield = self.__new_field
        else:
            newfield = copy.deepcopy(self.__field)

        col = ls.get_available_column(newfield, y, x)
        if not col:
            return

        # двигаем согласно sd
        if sd == ShiftDirection.UP:
            # сохраняем 1 элемент
            i = newfield[col[0]][x].value
            for t in range(col[0], col[1]):
                newfield[t][x].value = newfield[t+1][x].value
            newfield[col[1]][x].value = i
        if sd == ShiftDirection.DOWN:
            # сохраняем последний элемент
            i = newfield[col[1]][x].value
            for t in range(col[1], col[0], -1):
                newfield[t][x].value = newfield[t-1][x].value
            newfield[col[0]][x].value = i


        # Найдем возможные ходы
        self.__sequences = []
        [self.__sequences.append(i) for i in Game.find_seqs(newfield, sf.RowSequenceFmt)]
        [self.__sequences.append(i) for i in Game.find_seqs(list(zip(*newfield)), sf.ColSequenceFmt)]

        # заполним изменившуюся матрицу
        self.__new_field = newfield

    # пересекается ли текущая последовательность с уже удаленными
    # возможно, чтобы не пложить условия, стоило бы генерировать точки
    # для сверяемых послед. и сравнивать.
    @staticmethod
    def __is_seq_intersect(deleted, seq):
        for s in deleted:
            # удаленный шаг лежал по горизонтали
            if s[3] == 0:
                if (seq[1] >= s[1]) and (seq[1] <= s[1] + s[2] - 1) and s[0] >= seq[0]:
                    return True
            # удаленный шаг лежал по вертикали
            if s[3] == 1:
                if s[0] <= seq[0] and (s[1] >= seq[1]) and (s[1] <= seq[1] + seq[2] - 1):
                    return True
        return False

    # Применяем шаги
    def apply(self):
        # Удаляем
        deleted = []
        for seq in self.__sequences:
            # если шаг не был затронут ранее
            if not Game.__is_seq_intersect(deleted, seq):
                deleted.append(seq)
                # шаг по горизонтали
                if seq[3] == 0:
                    # бежим по отрезку
                    for x in range(seq[1], seq[1] + seq[2]):
                        self.item(seq[0], x).is_deleted = True
                        # получаем столбец, куда нужно докинуть сверху итем
                        col = ls.get_available_column(self.__new_field, seq[0], x)
                        # shift
                        for i in range(seq[0], col[0], -1):
                            self.__new_field[i][x].value = self.__new_field[i-1][x].value
                        # докинули сверху
                        self.__new_field[col[0]][x].value = random.choice(Game.item_values())
                # шаг по вертикали
                if seq[3] == 1:
                    for y in range(seq[0], seq[0] + seq[2]):
                        self.item(y, seq[1]).is_deleted = True
                    # столбец, куда докидываем
                    col = ls.get_available_column(self.__new_field, seq[0], seq[1])
                    for y in range(col[0], seq[0]):
                        self.__new_field[y + seq[2]][seq[1]].value = self.__new_field[y][seq[1]].value
                        self.__new_field[y][seq[1]].value = random.choice(Game.item_values())

        # разобьем вновь образовавшиеся готовые послед.
        seqs = []
        # по строкам
        [seqs.append(i) for i in Game.find_seqs(self.__new_field, sf.RowSequenceFmt)]
        # по столбцам
        [seqs.append(i) for i in Game.find_seqs(list(zip(*self.__new_field)), sf.ColSequenceFmt)]
        # # anti-random
        while len(seqs) != 0:
            for i in seqs:
                if i[3] == 0:
                    for v in range(i[1]+i[2]):
                        self.__new_field[i[0]][v].value = random.choice(Game.item_values())
                if i[3] == 1:
                    for v in range(i[0] + i[2]):
                        self.__new_field[v][i[1]].value = random.choice(Game.item_values())
            seqs.clear()
            # по строкам
            [seqs.append(i) for i in Game.find_seqs(self.__new_field, sf.RowSequenceFmt)]
            # по столбцам
            [seqs.append(i) for i in Game.find_seqs(list(zip(*self.__new_field)), sf.ColSequenceFmt)]

        self.__sequences = None
        self.__field = self.__new_field
        self.__new_field = None

    # Восстанавливаем исходную матрицу
    def discard(self):
        self.__new_field = None

