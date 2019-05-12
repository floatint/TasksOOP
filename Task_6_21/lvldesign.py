# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lvldesign.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from Task_6_21.ui.ui_lvldesign import Ui_ConstructorWindow
from PyQt5 import QtGui, QtWidgets


class ConstructorWindow(QtWidgets.QMainWindow, Ui_ConstructorWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.selectedcolor = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        self.color = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        self.levelview.setStyleSheet('QTableView { gridline-color: red; }')
        self.levelview.itemClicked.connect(self.cell_click)
        self.addrow.triggered.connect(self.add_row)
        self.addcol.triggered.connect(self.add_col)
        self.delrow.triggered.connect(self.del_row)
        self.delcol.triggered.connect(self.del_col)
        self.save.triggered.connect(self.save_level)
        self.clear.triggered.connect(self.clear_level)
        for y in range(self.levelview.rowCount()):
            for x in range(self.levelview.columnCount()):
                i = QtWidgets.QTableWidgetItem('')
                self.levelview.setItem(y, x, i)

    def cell_click(self, item):
        if item.background() == self.selectedcolor:
            item.setBackground(self.color)
        else:
            item.setBackground(self.selectedcolor)
        self.levelview.clearSelection()

    # что то со  стобцом при расчете ширины
    def constructor_resize(self):
        self.levelview.resizeRowsToContents()
        self.levelview.resizeColumnsToContents()
        # считаем ширину и высоту карты
        w = self.levelview.verticalHeader().sectionSize(0) * self.levelview.columnCount()
        h = self.levelview.horizontalHeader().sectionSize(0) * self.levelview.rowCount()
        # подгонка размера
        self.levelview.setSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.levelview.setFixedSize(w + 62, h + 64)
        # размер окошка основного
        self.setFixedSize(w, h + 24)

    def add_row(self):
        self.levelview.setRowCount(self.levelview.rowCount() + 1)
        y = self.levelview.rowCount() - 1
        for x in range(self.levelview.columnCount()):
            i = QtWidgets.QTableWidgetItem('')
            self.levelview.setItem(y, x, i)
        self.constructor_resize()

    def add_col(self):
        self.levelview.setColumnCount(self.levelview.columnCount() + 1)
        x = self.levelview.columnCount() - 1
        for y in range(self.levelview.rowCount()):
            i = QtWidgets.QTableWidgetItem('')
            self.levelview.setItem(y, x, i)
        self.constructor_resize()

    def del_col(self):
        self.levelview.setColumnCount(self.levelview.columnCount() - 1)
        self.constructor_resize()

    def del_row(self):
        self.levelview.setRowCount(self.levelview.rowCount() - 1)
        self.constructor_resize()

    def save_level(self):
        filename = QtWidgets.QFileDialog.getSaveFileName()[0]

        if not filename:
            return
        try:
            with open(filename, "w+") as lvl:
                for y in range(self.levelview.rowCount()):
                    for x in range(self.levelview.columnCount()):
                        lvl.write(str(int(self.levelview.item(y, x).background() == self.selectedcolor)))
                    if y != self.levelview.rowCount() - 1:
                        lvl.write('\n')
        except Exception as ex:
            print("Save level error. " + str(ex))

    def clear_level(self):
        for y in range(self.levelview.rowCount()):
            for x in range(self.levelview.columnCount()):
                self.levelview.item(y, x).setBackground(self.color)

