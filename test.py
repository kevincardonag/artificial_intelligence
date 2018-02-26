from constanst import *

matriz = [' '] * ROWS_NUMBER

for i in range(ROWS_NUMBER):
    matriz[i] = [' '] * COLUMNS_NUMBER


matriz[1][0] = "A"

for row in matriz:
    print(row, '\n')