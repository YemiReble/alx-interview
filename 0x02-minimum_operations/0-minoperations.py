#!/usr/bin/env python3
""" A function that calculate the minimum
operation of a given task
"""


def minOperations(n):
    """
        Calculates the minimum number of operations required
        to perform the given task.

        Parameters: n (int): An integer specifying the task
        to perform.

        Returns: int: The minimum number of operations required
            to perform the task.
    """
    alphabet = "H"
    operations = 1
    current_string = alphabet
    while len(current_string) < n:
        if len(current_string) * 2 <= n:
            current_string = current_string * 2
            operations += 0
        else:
            if len(current_string) == n:
                break
        current_string += alphabet
        operations += 1
    # Disclaimer This Method doesn't work as expected
    return operations
