from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(642, 684)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gameviewer = QtWidgets.QTableWidget(self.centralwidget)
        self.gameviewer.setGeometry(QtCore.QRect(0, 0, 641, 661))
        self.gameviewer.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.gameviewer.setIconSize(QtCore.QSize(64, 64))
        self.gameviewer.setRowCount(0)
        self.gameviewer.setColumnCount(0)
        self.gameviewer.setObjectName("gameviewer")
        self.gameviewer.horizontalHeader().setVisible(False)
        self.gameviewer.horizontalHeader().setDefaultSectionSize(64)
        self.gameviewer.horizontalHeader().setHighlightSections(False)
        self.gameviewer.horizontalHeader().setMinimumSectionSize(64)
        self.gameviewer.verticalHeader().setVisible(False)
        self.gameviewer.verticalHeader().setDefaultSectionSize(64)
        self.gameviewer.verticalHeader().setHighlightSections(False)
        self.gameviewer.verticalHeader().setMinimumSectionSize(64)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 642, 21))
        self.menubar.setObjectName("menubar")
        self.menugame = QtWidgets.QMenu(self.menubar)
        self.menugame.setObjectName("menugame")
        self.menulevel = QtWidgets.QMenu(self.menubar)
        self.menulevel.setObjectName("menulevel")
        self.menusettings = QtWidgets.QMenu(self.menubar)
        self.menusettings.setObjectName("menusettings")
        MainWindow.setMenuBar(self.menubar)
        self.newgame = QtWidgets.QAction(MainWindow)
        self.newgame.setObjectName("newgame")
        self.loadlevel = QtWidgets.QAction(MainWindow)
        self.loadlevel.setObjectName("loadlevel")
        self.loadlevel.triggered.connect(self.load_lvl)
        self.construct = QtWidgets.QAction(MainWindow)
        self.construct.setObjectName("construct")
        self.construct.triggered.connect(self.show_construct)
        self.menugame.addAction(self.newgame)
        self.menulevel.addAction(self.loadlevel)
        self.menusettings.addAction(self.construct)
        self.menubar.addAction(self.menugame.menuAction())
        self.menubar.addAction(self.menulevel.menuAction())
        self.menubar.addAction(self.menusettings.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Игра столетия"))
        self.menugame.setTitle(_translate("MainWindow", "Игра"))
        self.menulevel.setTitle(_translate("MainWindow", "Уровень"))
        self.menusettings.setTitle(_translate("MainWindow", "Настройки"))
        self.newgame.setText(_translate("MainWindow", "Новая"))
        self.loadlevel.setText(_translate("MainWindow", "Загрузить"))
        self.construct.setText(_translate("MainWindow", "Конструктор"))