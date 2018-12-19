import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from ui import Ui_MainWindow
import random

class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.tips.setText('Нажмите START для начала игры...')
        self.btn1.clicked.connect(self.start)
        self.btn2.clicked.connect(self.info)
        self.levels = [(100, random.randint(1,3)),
                       (500, random.randint(5,10)),
                       (10000, random.randint(10,50)),
                       (1000000, random.randint(50,100)),
                       (1000000000, random.randint(100, 1000))]
    def info(self):
        self.main_scene.setPlainText('Producer: Timerkhan Giniyatyllin\nWriter: Irek Valeev')

    def start(self):
        with open('text', 'r') as text:
            text = text.read()
        self.main_scene.setPlainText(text)
        self.btn1.setText('FIGHT')
        self.btn2.setText('NEXT')
        self.sila = 1
        for i in range(5):
            while self.sila < self.levels[i][0]:
                self.btn2.clicked.connect(self.attack)
                print(self.sila)
    def IsTrue(self, sila, lvl):
        if sila >= self.levels[lvl]:
            return True
        else:
            return False
    def attack(self):
        for i in range(self.levels):
            if self.sila < self.levels[i][0]:
                self.sila += self.levels[i][1]
                break
        print(self.sila)
app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
