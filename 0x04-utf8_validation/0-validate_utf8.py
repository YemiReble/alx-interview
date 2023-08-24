#!/usr/bin/python3
"""
A method that determines if a given data set
represents a valid UTF-8 encoding.

Prototype: def validUTF8(data)
Return: True if data is a valid UTF-8 encoding,
        else return False

A character in UTF-8 can be 1 to 4 bytes long
The data set can contain multiple characters
The data will be represented by a list of integers
Each integer represents 1 byte of data, therefore you
only need to handle the 8 least significant bits of
each integer.
"""


def validUTF8(data):
    """
    A function that validates
    a dataset and check if the
    dataset is UTF8
    """
    data = iter(data)
    for leading_byte in data:
        leading_ones = count_leading_ones(leading_byte)
        if leading_ones in [1, 7, 8]:
            return False
        for _ in range(leading_ones - 1):
            trailing_byte = next(data, None)
            if trailing_byte is None or trailing_byte >> 6 != 0b10:
                return False
    return True


def count_leading_ones(byte):
    for i in range(8):
        if byte >> (7 - i) == 0b11111111 >> (7 - i) & ~1:
            return i
    return 8
