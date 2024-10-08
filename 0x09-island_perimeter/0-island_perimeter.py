#!/usr/bin/python3
""" returns the perimeter of the island described in grid """


def island_perimeter(grid):
    """ return perimeter of island """
    perim = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                perim += 4
                if i > 0 and grid[i-1][j] == 1:
                    perim -= 2
                if j > 0 and grid[i][j-1] == 1:
                    perim -= 2
    return perim
