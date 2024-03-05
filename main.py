import sys
import numpy as np
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem


def tableToMatrix(matrix):
    if matrix.rowCount() != 1 and matrix.columnCount() != 1:

        return np.array([[float(matrix.item(i, j).text())
                          for j in range(matrix.columnCount())]
                         for i in range(matrix.rowCount())])

    return int(matrix.item(0, 0).text())


class MatrixCalculator(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("MatrixCalculator.ui", self)
        self.result = None
        self.np_matrix1, self.np_matrix2 = None, None
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Matrix Calculator')
        self.Run()

    def Run(self):
        self.bt_add_row1.clicked.connect(self.manipTableSize)
        self.bt_add_col1.clicked.connect(self.manipTableSize)

        self.bt_del_col1.clicked.connect(self.manipTableSize)
        self.bt_del_row1.clicked.connect(self.manipTableSize)

        self.bt_add_row2.clicked.connect(self.manipTableSize)
        self.bt_add_col2.clicked.connect(self.manipTableSize)

        self.bt_del_row2.clicked.connect(self.manipTableSize)
        self.bt_del_col2.clicked.connect(self.manipTableSize)

        self.bt_reset1.clicked.connect(self.resetTableData)
        self.bt_reset2.clicked.connect(self.resetTableData)

        self.calculate.clicked.connect(self.ShowCalculations)

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

    def resetTableData(self):
        sender = self.sender()

        if sender.accessibleName() == "reset1":
            table = self.matrix1
        else:
            table = self.matrix2

        for i in range(table.rowCount()):
            for j in range(table.columnCount()):
                table.setItem(i, j, None)

    def manipTableSize(self):

        sender = self.sender()
        if sender.accessibleName().startswith("m1"):
            matrix = self.matrix1
            matrix_num = "1"
        else:
            matrix = self.matrix2
            matrix_num = "2"

        if sender.accessibleName() == f"m{matrix_num} row":
            matrix.setRowCount(matrix.rowCount() + 1)

        elif sender.accessibleName() == f"m{matrix_num} row del":
            matrix.setRowCount(matrix.rowCount() - 1)

        elif sender.accessibleName() == f"m{matrix_num} col":
            matrix.setColumnCount(matrix.columnCount() + 1)

        elif sender.accessibleName() == f"m{matrix_num} col del":
            matrix.setColumnCount(matrix.columnCount() - 1)

    def ShowCalculations(self):
        print(type(self.result))
        if type(self.result) == float:
            print(f"{self.result} is float typed")

        else:
            row, col = self.result.shape
            print(row, col)
            for i in range(row):
                for j in range(col):
                    print(f"{self.result[i, j]}", end="  ")
                print()
            print()

    def operationToDo(self):
        sender = self.sender()
        # TODO акрнуть tableToMatrix(arg) в класс
        #  Построить логику проверки транспозиции до перевода маьрицы в MumPy

        self.np_matrix1 = tableToMatrix(self.matrix1)
        self.np_matrix2 = tableToMatrix(self.matrix2)

        if sender.accessibleName() == "summation":

            if self.checkDimension():
                self.result = self.np_matrix1 + self.np_matrix2
                self.ShowCalculations()

        elif sender.accessibleName() == "subtraction":

            if self.checkDimension():
                self.result = self.np_matrix1 - self.np_matrix2
                self.ShowCalculations()

        elif sender.accessibleName() == "multiplication":

            if self.checkMultiplication():
                # TODO оформить вывод ответа или ошибок в новое окно по нажатию кнопки
                self.result = self.np_matrix1.dot(self.np_matrix2)
                self.ShowCalculations()

        elif sender.accessibleName() == "determinant":

            det = np.linalg.det(self.np_matrix1)
            self.result = float(f"{det:.3f}")

            self.ShowCalculations()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    ex = MatrixCalculator()
    ex.show()
    sys.exit(app.exec())
