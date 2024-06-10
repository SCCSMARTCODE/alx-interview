#!/usr/bin/python3
"""
This is the module that contains the rotate_2d_matrix function definition
"""


def rotate_2d_matrix(matrix: list[list, ...]) -> None:
    """
    This function rotates a matrix
    :param matrix:
    :return: None
    """
    matrix_form_holder = [x.copy() for x in matrix]
    matrix_len = len(matrix)

    for row in range(matrix_len):
        for column in range(matrix_len):
            matrix[row][column] = matrix_form_holder[matrix_len - column - 1][row]
