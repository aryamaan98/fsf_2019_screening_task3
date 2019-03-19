from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


from MainWindow import Ui_Steel

class MainWindow(QMainWindow, Ui_Steel):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        
        self.show()


if __name__ == "__main__":
    import sys
    app = QApplication([])
    window = MainWindow()
    sys.exit(app.exec_())

