#!/usr/bin/python3
""" a module that creates and maps out a pascal triangle """


def pascal_triangle(n):
    """ method that creates and maps out a pascal triangle:
    """
    pascalTriange = []
    if (n <= 0):
        return pascalTriange

    else:
        for i in range(1, n + 1):
            temp = []
            val = 1
            for k in range(1, (i + 1)):
                temp.append(val)
                val = val * (i - k) // k
            pascalTriange.append(temp)
    return pascalTriange
