import csv
import sys

from PyQt5 import uic
from PyQt5.Qt import QHeaderView
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem


class MatrixCalculator(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("MatrixCalculator.ui", self)
        self.prise_list = {}
        self.Operation_for_now = None
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Matrix Calculator')
        self.Run()

    def Run(self):
        self.bt_add_row1.clicked.connect(self.MatrixAdd)
        self.bt_add_row2.clicked.connect(self.MatrixAdd)
        self.bt_add_col1.clicked.connect(self.MatrixAdd)
        self.bt_add_col2.clicked.connect(self.MatrixAdd)

        self.summation.toggled.connect(self.OperationToDo)
        self.multiplication.toggled.connect(self.OperationToDo)
        self.subtraction.toggled.connect(self.OperationToDo)
        self.determinant.toggled.connect(self.OperationToDo)

    def CheckMultiplication(self):
        for i in range(self.matrix1.rowCount()):
            for j in range(self.matrix1.rowCount()):
                print(self.matrix1.item(i, j).text(), end=" ")
            print()

    def MatrixAdd(self):
        sender = self.sender()
        if sender.accessibleName() == "m1 row":
            self.matrix1.setRowCount(self.matrix1.rowCount() + 1)

        elif sender.accessibleName() == "m1 col":
            self.matrix1.setColumnCount(self.matrix1.columnCount() + 1)

        elif sender.accessibleName() == "m2 row":
            self.matrix2.setRowCount(self.matrix2.rowCount() + 1)

        elif sender.accessibleName() == "m2 col":
            self.matrix2.setColumnCount(self.matrix2.columnCount() + 1)

    def OperationToDo(self):
        sender = self.sender()
        if sender.accessibleName() == "summation":
            self.Operation_for_now = "summation"

        elif sender.accessibleName() == "multiplication":
            self.CheckMultiplication()
            self.Operation_for_now = "multiplication"

        elif sender.accessibleName() == "subtraction":
            self.Operation_for_now = "subtraction"

        elif sender.accessibleName() == "determinant":
            self.Operation_for_now = "determinant"


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    ex = MatrixCalculator()
    ex.show()
    sys.exit(app.exec())
