from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox
import sys

class InfoWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Information')
        self.setGeometry(100,100,680,500)