#!/usr/bin/python3
""" return pascal triangle """


def pascal_triangle(n):
    """ returns list of lists rep Pascal's triangle of n """
    if n <= 0:
        return []

    triangle = [[1]]

    for a in range(1, n):
        row = [1]
        for b in range(1, a):
            row.append(triangle[a - 1][b - 1] + triangle[a - 1][b])
        row.append(1)
        triangle.append(row)
    return triangle
