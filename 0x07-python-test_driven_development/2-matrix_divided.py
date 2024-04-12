#!/usr/bin/python3
'''
    A module that divides all element of a matrix of matrixs by a given value.
'''


def matrix_divided(matrix, div):
    '''
        Function that divides all element of a given matrix.
        Args:
        matrix: a matrice of matrices.
        div: given value to divide by.
    '''
    for item in matrix:
        for number in item:
            if not isinstance(number, (int, float)):
                raise TypeError('''matrix must be a matr
                        ix (list of lists) of integers/floats''')
    sub_matrix_lengths = [len(sub_matrix) for sub_matrix in matrix]
    if (min(sub_matrix_lengths) != max(sub_matrix_lengths)):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    result = [[round(number / div, 2) for number in item] for item in matrix]
    return result
