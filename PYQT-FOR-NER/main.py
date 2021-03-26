import sys

from PyQt5 import uic
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *

import file_open_easygui as fopen

form_class = uic.loadUiType("main_window.ui")[0]


class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.loadButton.clicked.connect(self.loadButtonFunction)

    def loadButtonFunction(self):
        print("LOAD Button Clicked.")
        absPath = fopen.OpenWinFileExplorer()
        print(absPath)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
