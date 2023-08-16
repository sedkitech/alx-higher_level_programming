#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = []
    for row in matrix:
        row = list(map(lambda x: x * x, row))
        new.append(row)
    return new
