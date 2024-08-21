#!/usr/bin/python3
""" calculate fewest number of operations needed to result
in exactily n H characters in the file
"""


def minOperations(n):
    if n <= 1:
        return 0

    opers = 0
    fac = 2
    while n > 1:
        while n % fac == 0:
            n /= fac
            opers += fac
        fac += 1
    return opers
