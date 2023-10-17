import csv
import sys
import numpy as np
from PyQt5 import uic
from PyQt5.Qt import QHeaderView
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem


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

    def tableToMatrix(self, matrix):  # get matrix
        list_matrix = []
        list_row_matrix = []
        for i in range(matrix.rowCount()):
            for j in range(matrix.rowCount()):  # apply to it methods,
                list_row_matrix.append(int(matrix.item(i, j).text()))

            list_matrix.append(list_row_matrix)
            list_row_matrix = []

        return np.array(list_matrix)  # returns NumPy

    def checkMultiplication(self):
        if self.matrix1.columnCount() == self.matrix2.rowCount():
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
        np_matrix1 = self.tableToMatrix(self.matrix1)
        np_matrix2 = self.tableToMatrix(self.matrix2)

        if sender.accessibleName() == "summation":
            print(np_matrix1 + np_matrix2)
            self.operation_for_now = "summation"

        # TODO Построить архетиктуру, соединить с логическимим функциями
        elif sender.accessibleName() == "subtraction":
            print(np_matrix1 - np_matrix2)
            self.operation_for_now = "subtraction"

        elif sender.accessibleName() == "multiplication":
            if self.checkMultiplication():
                # TODO оформить вывод ответа или ошибок в новое окно по нашатию кнопки
                print(np_matrix1.dot(np_matrix2))  # cmd output of multiplied matrix
            self.operation_for_now = "multiplication"

        elif sender.accessibleName() == "determinant":
            # TODO Сделать что бы при выбори детерменанты вторая матрица становилась не изменяемой и исчезала
            print(np.linalg.det(np_matrix1))
            self.operation_for_now = "determinant"


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    ex = MatrixCalculator()
    ex.show()
    sys.exit(app.exec())
