def generate_solutions(n, columns):
    """Generate all solutions to the N-queens problem.

    Args:
        n: The number of queens.
        columns: A list of the column indices of the queens, where columns[i] is the column index of the queen in row i.

    Returns:
        A list of lists, where each sublist represents a solution to the N-queens problem.
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
        columns: A list of the column indices of the queens, where columns[i] is the column index of the queen in row i.

    Returns:
        True if it is safe to place a queen at the given row and column, False otherwise.
    """

    for i in range(row):
        if columns[i] == column or abs(columns[i] - column) == row - i:
            return False

    return True


def main():
    n = int(input("Enter the number of queens: "))

    columns = [-1] * n

    solutions = generate_solutions(n, columns)

    print("There are {} solutions to the {}-queens problem.".format(len(solutions), n))

    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()
