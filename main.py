import csv
import sys

from PyQt5 import uic
from PyQt5.Qt import QHeaderView
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem


class Bill(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("matrix_calc.ui", self)
        self.prise_list = {}

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Интерактивный чек')







if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    ex = Bill()
    ex.show()
    sys.exit(app.exec())
