#!/usr/bin/python3
"""
Island Perimeter
"""


def check_val(x):
    """ Checks if the input value is 0 or 1 and returns
        1 if it is 0, 0 if it is 1, or 1 if it is not 0 or 1.
    """
    if x == 0:
        return 1
    return 0

def island_perimeter(grid):
    """ Calculates the perimeter of the island by traversing
        the grid and checking the values of each cell.
    """
    row = len(grid)
    col = len(grid[0])
    assert (1 <= row and col <= 100), "row and col must be between 1 and 100"

    x = 0
    for i in range(row):
        for j in range(col):
            if grid[i][j] == 1:
                if i-1 < 0:
                    x += 1
                else:
                    x += check_val(grid[i-1][j])
                if j-1 < 0:
                    x += 1
                else:
                    x += check_val(grid[i][j-1])

                try:
                    x += check_val(grid[i+1][j])
                except IndexError:
                    x += 1
                try:
                    x += check_val(grid[i][j+1])
                except IndexError:
                    x += 1

    return x
