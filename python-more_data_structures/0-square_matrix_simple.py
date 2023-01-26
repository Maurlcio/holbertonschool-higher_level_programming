#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for col in matrix:
        for row in range(len(col)):
            new_matrix.append(col[row] ** 2)
    return new_matrix
