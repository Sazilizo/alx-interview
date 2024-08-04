#!/usr/bin/python3
"""
0-UTF-8 Validation
"""


def validUTF8(data):
    """
    Data: a list of integers
    Return: True if data is a valid UTF-8
    encoding, else return False
    """
    bytes = 0

    for byte in data:
        if bytes == 0:
            if byte >> 5 == 0b110 or byte >> 5 == 0b1110:
                bytes = 1
            elif byte >> 4 == 0b1110:
                bytes = 2
            elif byte >> 3 == 0b11110:
                bytes = 3
            elif byte >> 7 == 0b1:
                return False
        else:
            if byte >> 6 != 0b10:
                return False
            bytes -= 1
    return bytes == 0
