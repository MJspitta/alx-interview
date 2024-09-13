#!/usr/bin/python3
""" solves the N-queens puzzle """
import sys


def is_safe(brd, row, col):
    """ if queen can be placed on board """
    for i in range(row):
        if brd[i] == col or \
           brd[i] - i == col - row or \
           brd[i] + i == col + row:
               return False
    return True

def sol_nqueens(brd, row, N):
    if row == N:
        print([[i, brd[i]] for i in range(N)])
        return
    for col in range(N):
        if is_safe(brd, row, col):
            brd[row] = col
            sol_nqueens(brd, row + 1, N)
            brd[row] = -1

def nqueens(N):
    brd = [-1 for _ in range(N)]
    sol_nqueens(brd, 0, N)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        N = int(sys.argv[1])
    except ValeError:
        print("N must be a number")
        sys.exit(1)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)
    nqueens(N)
