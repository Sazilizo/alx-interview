#!/usr/bin/python3
"""Rotates a 2D Matrix"""


def rotate_2d_matrix(matrix):
    """rotates a 2D matrix 90 degrees clockwise"""
    length = len(matrix)
    for x in range(0, int(length / 2)):
        for y in range(x, length - x - 1):
            temp = matrix[x][y]
            matrix[x][y] = matrix[length - 1 - y][x]
            matrix[length - 1 - y][x] = matrix[length - 1 - x][length - 1 - y]
            matrix[length - 1 - x][length - 1 - y] = matrix[y][length - 1 - x]
            matrix[y][length - 1 - x] = temp
            