#!/usr/bin/python3
""" rotate 2D matrix 90 degrees clockwise """


def rotate_2d_matrix(matrix):
    """ rotate matrix clockwise """
    matrixLen = len(matrix)

    for i in range(matrixLen):
        for j in range(i, matrixLen):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(matrixLen):
        matrix[i].reverse()
