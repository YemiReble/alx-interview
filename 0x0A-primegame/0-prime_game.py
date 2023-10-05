#!/usr/bin/python3
"""
Prime Game
"""


def isWinner(x, nums):
    """
    Determine the winner of the game given the number of
    rounds and the set of numbers.

    Args:
      x: The number of rounds.
      nums: An array of consecutive integers starting from 1
      up to and including n, where n is the number of numbers in the set.

    Returns:
      The name of the player that won the most rounds, or None if the
      winner cannot be determined.
    """

    # Initialize the players' scores.
    maria_score = 0
    ben_score = 0

    # Play the game.
    for i in range(x):
        # Maria's turn.
        maria_move = get_maria_move(nums)
        if maria_move is None:
            # Maria cannot make a move, so Ben wins.
            ben_score += 1
            break

        # Remove the chosen number and its multiples from the set.
        nums = remove_multiples(nums, maria_move)

        # Ben's turn.
        ben_move = get_ben_move(nums)
        if ben_move is None:
            # Ben cannot make a move, so Maria wins.
            maria_score += 1
            break

        # Remove the chosen number and its multiples from the set.
        nums = remove_multiples(nums, ben_move)

    # Determine the winner.
    if maria_score > ben_score:
        return "Maria"
    elif ben_score > maria_score:
        return "Ben"
    else:
        return None


def get_maria_move(nums):
    """
    Get Maria's next move.

    Args:
      nums: An array of consecutive integers starting from 1 up to and
      including n, where n is the number of numbers in the set.

    Returns:
      The next number that Maria should choose, or None if there are
      no prime numbers left.
    """

    # Find the smallest prime number in the set.
    smallest_prime = None
    for num in nums:
        if is_prime(num):
            smallest_prime = num
            break

    # If there is no prime number left, return None.
    if smallest_prime is None:
        return None

    return smallest_prime


def get_ben_move(nums):
    """
    Get Ben's next move.

    Args:
      nums: An array of consecutive integers starting from 1 up to and
      including n, where n is the number of numbers in the set.

    Returns:
      The next number that Ben should choose, or None if there are no
      numbers left.
    """

    # If there is only one number left, Ben chooses that number.
    if len(nums) == 1:
        return nums[0]

    # Otherwise, Ben chooses the largest number in the set.
    largest_number = max(nums)
    return largest_number


def remove_multiples(nums, number):
    """
    Remove the given number and its multiples from the set.

    Args:
      nums: An array of consecutive integers starting from 1 up to and
      including n, where n is the number of numbers in the set.
      number: The number to remove and its multiples.

    Returns:
      An array of the remaining numbers in the set.
    """

    new_nums = []
    for num in nums:
        if num % number != 0:
            new_nums.append(num)

    return new_nums


def is_prime(number):
    """
    Check if a number is prime.

    Args:
      number: The number to check.

    Returns:
      True if the number is prime, False otherwise.
    """

    if number <= 1:
        return False

    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False

    return True
