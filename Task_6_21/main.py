# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtWidgets
from Task_6_21.mainwindow import MainWindow
import traceback
import sys


def exception_hook(type_, value, tb):
    msg = '\n'.join(traceback.format_exception(type_, value, tb))
    # print(msg)
    QtWidgets.QMessageBox.critical(None, 'Unhandled top level exception', msg)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    sys.excepthook = exception_hook
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec_())

