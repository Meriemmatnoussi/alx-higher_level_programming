#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = []
    for numbers in matrix:
        new.append([numbers[i] * numbers[i]for i in range(len(numbers))])
    return new
