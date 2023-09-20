#!/usr/bin/python3
""" This Script Creates an Algorithm that
determine the fewest number of coins needed
to meet a given amount total
"""


def makeChange(coins, total):
    """
    Calculates the fewest number of coins needed to make the given amount.

    Returns:
      The fewest number of coins needed to make the given amount, or -1 if the
      amount cannot be made.
    """
    table = [float('inf')] * (total + 1)

    table[0] = 0
    table[1] = 1

    for i in range(2, total + 1):
        for coin in coins:
            if i - coin >= 0:
                table[i] = min(table[i], table[i - coin] + 1)

    return table[total]
