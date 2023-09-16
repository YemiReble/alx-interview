#!/usr/bin/python3
"""
Solving N queens
NOTE: This solution me took me few week to complete
    and was eventually completed with the help
    of Google Bard AI. All documentation was
    written by the said AI.
"""


import sys


def generate_solutions(n, columns):
    """Generate all solutions to the N-queens problem.

    Args:
        n: The number of queens.
        columns: A list of the column indices of the queens,
        where columns[i] is the column index of the queen in row i.

    Returns:
        A list of lists, where each sublist represents a solution
        to the N-queens problem in the specified format.
    """

    solutions = []

    def place_queen(row):
        if row == n:
            solutions.append(columns[:])
            return

        for column in range(n):
            if is_safe(row, column, columns):
                columns[row] = column
                place_queen(row + 1)

    place_queen(0)
    return solutions


def is_safe(row, column, columns):
    """Check if it is safe to place a queen at the given row and column.

    Args:
        row: The row index.
        column: The column index.
        columns: A list of the column indices of the queens, where
            columns[i] is the column index of the queen in row i.

    Returns:
        True if it is safe to place a queen at the given row and
        column, False otherwise.
    """

    for i in range(row):
        if columns[i] == column or abs(columns[i] - column) == row - i:
            return False

    return True


def logic():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit():
        n = int(sys.argv[1])
    else:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    return (n)


def main():
    n = logic()
    columns = [-1] * n

    solutions = generate_solutions(n, columns)

    for solution in solutions:
        new_solution = []
        for row, column in enumerate(solution):
            new_solution.append([row, column])
        print(new_solution)


if __name__ == "__main__":
    main()
