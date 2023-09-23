def makeChange(coins, total):
  """
  Calculates the fewest number of coins needed to make the given amount.

  Returns:
    The fewest number of coins needed to make the given amount, or -1 if the
    amount cannot be made.
  """

  # Create a table to store the fewest number of coins needed to make each
  # amount.
  table = [float('inf')] * (total + 1)

  # Initialize the base case.
  table[0] = 0

  # Iterate over the total amount and calculate the fewest number of coins
  # needed to make each amount.
  for i in range(1, total + 1):
    for coin in coins:
      if i - coin >= 0:
        table[i] = min(table[i], table[i - coin] + 1)

  # If the value at table[total] is still infinity, then the total amount
  # cannot be made using the coins in the list.
  if table[total] == float('inf'):
    return -1

  # Return the fewest number of coins needed to make the given amount.
  return table[total]
