from Task_6_21.ui.ui_mainwindow import Ui_MainWindow
from Task_6_21.lvldesign import ConstructorWindow
from Task_6_21.game.game import Game, ShiftDirection
from PyQt5 import QtWidgets, QtGui, QtCore

# Работа с окошком
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        # vars
        self.item_width = 64
        self.item_height = 64
        self.level_path = None
        self.gameobject = None
        self.cur_item_index = None
        self.cw = None
        self.setupUi(self)
        self.newgame.triggered.connect(self.new_game)
        self.gameviewer.mousePressEvent = self.mouse_press
        self.gameviewer.mouseReleaseEvent = self.mouse_release
        self.gameviewer.mouseMoveEvent = self.mouse_move

        # Делегат отрисовки
        class GameItemDelegate(QtWidgets.QItemDelegate):
            def __init__(self, parent=None, *args):
                QtWidgets.QItemDelegate.__init__(self, parent, *args)

            def paint(self, painter: QtGui.QPainter, option: QtWidgets.QStyleOptionViewItem, idx: QtCore.QModelIndex):
                painter.save()
                self.parent().draw_item(idx, painter, option)
                self.parent().draw_steps(painter)
                painter.restore()

        self.gameviewer.setItemDelegate(GameItemDelegate(self))
        self.gameviewer.setShowGrid(False)

    # Рисование итема
    def draw_item(self, e: QtCore.QModelIndex, painter: QtGui.QPainter, option: QtWidgets.QStyleOptionViewItem):
        item = self.gameobject.item(e.row(), e.column())
        # итем особый
        if not item.is_available:
            painter.fillRect(option.rect, QtGui.QBrush(QtGui.QColor(0, 0, 0)))
            return
        if item.is_deleted:
            painter.fillRect(option.rect, QtGui.QBrush(QtGui.QColor(244, 241, 66)))
        else:
            # обычный итем
            painter.fillRect(option.rect, QtGui.QBrush(QtGui.QColor(127, 79, 51)))
        # дорисовываем картинку
        if item.value == 0:
            painter.setBrush(QtGui.QBrush(QtGui.QColor(249, 0, 0)))
            painter.drawEllipse(option.rect)
        if item.value == 1:
            painter.setBrush(QtGui.QBrush(QtGui.QColor(20, 0, 250)))
            painter.drawEllipse(option.rect)
        if item.value == 2:
            painter.setBrush(QtGui.QBrush(QtGui.QColor(41, 178, 43)))
            painter.drawEllipse(option.rect)

    # Обводка ходов
    def draw_steps(self, painter: QtGui.QPainter):
        if not self.gameobject.steps:
            return
        painter.setBrush(QtGui.QColor(0, 0, 0, 0))
        # painter.setPen(QtGui.QPen(QtCore.Qt.yellow, 2, QtCore.Qt.SolidLine))
        painter.setPen(QtGui.QPen(QtGui.QColor(186, 18, 155), 4, QtCore.Qt.SolidLine))
        for i in self.gameobject.steps:
            # расположен на строке
            if i[3] == 0:
                x = i[1]*self.item_width
                y = i[0]*self.item_height
                w = i[2] * self.item_width
                h = self.item_height
            if i[3] == 1:
                x = i[1]*self.item_width
                y = i[0]*self.item_height
                w = self.item_width
                h = i[2] * self.item_height
            painter.drawRect(x, y, w, h)

    # Показать конструктор
    def show_construct(self):
        self.cw = ConstructorWindow()
        self.cw.show()

    # Выброс сообщения
    @staticmethod
    def msgbox(msg):
        mb = QtWidgets.QMessageBox()
        mb.setText(msg)
        mb.exec()

    # Новая игра
    def new_game(self):
        if self.level_path:
            self.gameobject = self.create_game(self.level_path)
            self.game_view_resize()
            self.update_game_view()
        else:
            self.msgbox('Уровень не загружен')

    # Ресайз вью игрового поля
    def game_view_resize(self):
        width = self.gameobject.size["width"]
        height = self.gameobject.size["height"]
        # на всякий случай
        self.gameviewer.setRowCount(height)
        self.gameviewer.setColumnCount(width)
        self.gameviewer.resizeRowsToContents()
        self.gameviewer.resizeColumnsToContents()
        # считаем ширину и высоту карты
        w = self.gameviewer.verticalHeader().sectionSize(0) * self.gameviewer.columnCount()
        h = self.gameviewer.horizontalHeader().sectionSize(0) * self.gameviewer.rowCount()
        # подгонка размера
        self.gameviewer.setSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gameviewer.setFixedSize(w, h + 64)
        # размер окошка основного
        self.setFixedSize(w, h + 24)

    # Апдейт с перерисовкой итемов
    def update_game_view(self):
        self.gameviewer.viewport().update()

    # Подгрузка уровня и инициализация
    def create_game(self, path):
        try:
            go = Game(path)
        except Exception as ex:
            print("Ошибка создания игры. " + str(ex))
        return go

    # Загрузка уровня
    def load_lvl(self):
        # Загрузка
        fname = QtWidgets.QFileDialog.getOpenFileName()[0]

        if not fname:
            return

        self.gameobject = self.create_game(fname)
        self.game_view_resize()
        self.update_game_view()
        self.level_path = fname
        # матрица меняется - происходит апдейт
        # for y in range(5):
        #     for x in range(5):
        #         self.gameobject.item(y,x).is_deleted = True
        # self.update_game_view()

    def mouse_press(self, e: QtGui.QMouseEvent):
        if e.button() != QtCore.Qt.LeftButton:
            return
        if not self.gameobject:
            return
        # получили индекс элемента, с которого начинаем ход
        self.cur_item_index = (e.y() // self.item_height, e.x() // self.item_width)

    def mouse_move(self, e: QtGui.QMouseEvent):

        # игра не создана
        if not self.gameobject:
            return

        if not self.cur_item_index:
            return

        # получаем индекс итема под мышкой
        item_index = (e.y() // self.item_height, e.x() // self.item_width)

        # выход за границы поля.
        if (item_index[0] < 0 or item_index[1] < 0) or \
                (item_index[0] >= self.gameobject.size["height"] or item_index[1] >= self.gameobject.size["width"]):
            return

        if item_index == self.cur_item_index:
            return
        # проверяем направление движения
        # если двигаемся по строке
        if item_index[1] != self.cur_item_index[1]:
            # сдвиг влево
            if (item_index[1] - self.cur_item_index[1]) < 0:
                self.gameobject.row_shift(self.cur_item_index[0], self.cur_item_index[1], ShiftDirection.LEFT)
            # сдвиг в право
            if (item_index[1] - self.cur_item_index[1]) > 0:
                self.gameobject.row_shift(self.cur_item_index[0], self.cur_item_index[1], ShiftDirection.RIGHT)
        # если по столбцу
        if item_index[0] != self.cur_item_index[0]:
            # сдвиг вверх
            if (item_index[0] - self.cur_item_index[0]) < 0:
                self.gameobject.col_shift(self.cur_item_index[0], self.cur_item_index[1], ShiftDirection.UP)
            # сдвиг вниз
            if (item_index[0] - self.cur_item_index[0]) > 0:
                self.gameobject.col_shift(self.cur_item_index[0], self.cur_item_index[1], ShiftDirection.DOWN)

        self.cur_item_index = item_index
        # обновим поле
        self.update_game_view()

    def mouse_release(self, e: QtGui.QMouseEvent):
        if e.button() != QtCore.Qt.LeftButton:
            return
        if not self.gameobject:
            return

        # проверяем, образовались ли ходы ?
        if not self.gameobject.steps:
            # откат
            self.gameobject.discard()
        else:
            # применение ходов
            self.gameobject.apply()
        # обновим картинку
        self.update_game_view()

        # усли осилили
        if self.gameobject.is_complete:
            self.msgbox("Уровень закончен !")

        # Сбрасываем выбранное когда-то
        self.cur_item_index = None
