# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 400)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.main_scene = QtWidgets.QPlainTextEdit(self.centralWidget)
        self.main_scene.setGeometry(QtCore.QRect(10, 140, 580, 190))
        self.main_scene.setTabChangesFocus(True)
        self.main_scene.setLineWrapMode(QtWidgets.QPlainTextEdit.WidgetWidth)
        self.main_scene.setReadOnly(True)
        self.main_scene.setOverwriteMode(False)
        self.main_scene.setCenterOnScroll(True)
        self.main_scene.setPlaceholderText("")
        self.main_scene.setObjectName("main_scene")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralWidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 581, 121))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.funcs = QtWidgets.QComboBox(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.funcs.sizePolicy().hasHeightForWidth())
        self.funcs.setSizePolicy(sizePolicy)
        self.funcs.setObjectName("funcs")
        self.gridLayout.addWidget(self.funcs, 6, 1, 1, 1)
        self.btn = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn.sizePolicy().hasHeightForWidth())
        self.btn.setSizePolicy(sizePolicy)
        self.btn.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.btn.setAutoFillBackground(False)
        self.btn.setCheckable(False)
        self.btn.setAutoRepeat(False)
        self.btn.setAutoExclusive(False)
        self.btn.setAutoDefault(False)
        self.btn.setDefault(False)
        self.btn.setFlat(False)
        self.btn.setObjectName("btn")
        self.gridLayout.addWidget(self.btn, 5, 1, 1, 1)
        self.hp_text = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hp_text.sizePolicy().hasHeightForWidth())
        self.hp_text.setSizePolicy(sizePolicy)
        self.hp_text.setAlignment(QtCore.Qt.AlignCenter)
        self.hp_text.setObjectName("hp_text")
        self.gridLayout.addWidget(self.hp_text, 0, 0, 1, 1)
        self.hp = QtWidgets.QProgressBar(self.gridLayoutWidget)
        self.hp.setProperty("value", 100)
        self.hp.setObjectName("hp")
        self.gridLayout.addWidget(self.hp, 5, 0, 1, 1)
        self.tips = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tips.sizePolicy().hasHeightForWidth())
        self.tips.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.tips.setFont(font)
        self.tips.setTextFormat(QtCore.Qt.AutoText)
        self.tips.setAlignment(QtCore.Qt.AlignCenter)
        self.tips.setWordWrap(True)
        self.tips.setObjectName("tips")
        self.gridLayout.addWidget(self.tips, 6, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 600, 22))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn.setText(_translate("MainWindow", "btn"))
        self.hp_text.setText(_translate("MainWindow", "Здоровье"))
        self.tips.setText(_translate("MainWindow", "TextLabel"))


''