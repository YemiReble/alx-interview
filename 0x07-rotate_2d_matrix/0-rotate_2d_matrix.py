#!/usr/bin/python3
"""
This script rotate a 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """ Fucntion that rotates
        a 2D Matrix
    """
    temp_matrix = []
    col = len(matrix) - 1
    for col in range(len(matrix)):
        temp = []
        for row in range(len(matrix)-1, -1, -1):
            temp.append(matrix[row][col])
        temp_matrix.append(temp)
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            matrix[i][j] = temp_matrix[i][j]
    return matrix
