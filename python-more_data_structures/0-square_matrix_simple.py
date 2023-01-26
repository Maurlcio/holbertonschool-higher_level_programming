#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for col in matrix:
        other_block = []
        for row in col:
            other_block.append(row ** 2)
        new_matrix.append(other_block)
    return new_matrix
