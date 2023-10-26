import csv
import sys
import numpy as np
from PyQt5 import uic
from PyQt5.Qt import QHeaderView
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem

import numpy as np


def tableToMatrix(matrix):
    if matrix.rowCount() != 1 and matrix.columnCount() != 1:
        return np.array([[int(matrix.item(i, j).text())
                          for j in range(matrix.columnCount())]
                         for i in range(matrix.rowCount())])
    return int(matrix.item(0, 0).text())


class MatrixCalculator(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("MatrixCalculator.ui", self)
        self.operation_for_now = None
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Matrix Calculator')
        self.Run()

    def Run(self):
        self.bt_add_row1.clicked.connect(self.addToMatrix)
        self.bt_add_row2.clicked.connect(self.addToMatrix)

        self.bt_add_col1.clicked.connect(self.addToMatrix)
        self.bt_add_col2.clicked.connect(self.addToMatrix)

        self.summation.toggled.connect(self.operationToDo)
        self.multiplication.toggled.connect(self.operationToDo)
        self.subtraction.toggled.connect(self.operationToDo)
        self.determinant.toggled.connect(self.operationToDo)

    def checkMultiplication(self):
        if self.matrix1.columnCount() == self.matrix2.rowCount() or \
                (self.matrix2.rowCount() == 1 and self.matrix2.columnCount() == 1):
            return True
        return False

    def checkDimension(self):
        if self.matrix1.columnCount() == self.matrix2.columnCount() \
                and self.matrix1.rowCount() == self.matrix2.rowCount():
            return True
        return False

    def addToMatrix(self):
        sender = self.sender()
        if sender.accessibleName() == "m1 row":
            self.matrix1.setRowCount(self.matrix1.rowCount() + 1)

        elif sender.accessibleName() == "m1 col":
            self.matrix1.setColumnCount(self.matrix1.columnCount() + 1)

        elif sender.accessibleName() == "m2 row":
            self.matrix2.setRowCount(self.matrix2.rowCount() + 1)

        elif sender.accessibleName() == "m2 col":
            self.matrix2.setColumnCount(self.matrix2.columnCount() + 1)

    def operationToDo(self):
        sender = self.sender()
        np_matrix1 = tableToMatrix(self.matrix1)
        np_matrix2 = tableToMatrix(self.matrix2)

        if sender.accessibleName() == "summation":
            self.operation_for_now = "summation"

            if self.checkDimension():
                print(np_matrix1 + np_matrix2)

        elif sender.accessibleName() == "subtraction":
            self.operation_for_now = "subtraction"

            if self.checkDimension():
                print(np_matrix1 - np_matrix2)

        elif sender.accessibleName() == "multiplication":
            self.operation_for_now = "multiplication"

            if self.checkMultiplication():
                # TODO оформить вывод ответа или ошибок в новое окно по нашатию кнопки
                print(np_matrix1.dot(np_matrix2))  # cmd output of multiplied matrix

        elif sender.accessibleName() == "determinant":
            self.operation_for_now = "determinant"

            print(np.linalg.det(np_matrix1))

            self.matrix2.setRowCount(0)
            self.matrix2.setColumnCount(0)
            # TODO Привязвть показ к кнопки калбкуляции

            self.bt_add_col2.hide()
            self.bt_add_row2.hide()
            self.bt_del_col2.hide()
            self.bt_del_row2.hide()
            self.transpose2.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    ex = MatrixCalculator()
    ex.show()
    sys.exit(app.exec())
