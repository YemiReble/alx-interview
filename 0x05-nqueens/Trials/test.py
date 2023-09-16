#!/usr/bin/python3
import sys


def generate_solutions(row, column):
    if row == 0:
        return [[]]
    else:
        solutions = []
        prev_solution = []
        for queen in range(column):
            safe_positions = [x for x in range(column) if is_safe(queen, x, prev_solution)]
            for safe_position in safe_positions:
                new_solutions = place_queen(queen + 1, column, prev_solution + [safe_position])
                solutions.extend(new_solutions)
        return solutions


def place_queen(queen, column, prev_solution):
    new_solutions = []
    for array in prev_solution:
        for x in range(column):
            if is_safe(queen, x, array):
                new_solutions.append(array + [x])
    return new_solutions


def is_safe(q, x, array):
    for column in range(len(q)):
        if array[column] == x:
            return False
        if abs(array[column] - x) == q - column:
            return False
    return True


def init():
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


def n_queens():

    n = init()
    # generate all solutions
    solutions = generate_solutions(n, n)
    # print solutions
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    n_queens()

