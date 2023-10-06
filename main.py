import numpy as np
from sys import stdin
for _ in stdin:

    number_rows = int(input("input number of rows:"))

    matrix = []
    for i in range(number_rows):
        row = input(f"input matrix's {i+1} row data\n")

        matrix.append(list(map(lambda x: int(x), row.split())))

    matrix = np.array(matrix)

    print(matrix)
