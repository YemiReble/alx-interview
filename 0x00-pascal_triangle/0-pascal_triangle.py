#!/usr/bin/python3
""" Alx Interview Solution
    Create a function def pascal_triangle(n): that returns
    a list of lists of integers representing the Pascal’s
    triangle of n:

    Returns an empty list if n <= 0
    You can assume n will be always an integer
"""


def pascal_triangle(n):
    """Returns a list of lists of integers
    representing the Pascal's triangle of n."""
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n + 1):
        row = [1] * i
        for j in range(i):
            if j == 0 or j == i - 1:
                row[j] = 1
            else:
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)
    return triangle[1:]
