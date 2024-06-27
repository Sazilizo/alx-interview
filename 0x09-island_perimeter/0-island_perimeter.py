#!/usr/bin/python3
""" Island Perimeter """


def island_perimeter(grid):
    """ return the perimeter of the island described in grid """
    perimeter = 0

    for i, row in enumerate(grid):
        for j, element in enumerate(row):
            if (element == 0):
                continue

            if (j != 0 and row[j - 1] == 0):
                perimeter += 1
            if (j == 0):
                perimeter += 1

            if (row[j + 1] == 0 and j != len(row) - 1):
                perimeter += 1
            if (j == len(row) - 1):
                perimeter += 1

            if (i != 0 and grid[i - 1][j] == 0):
                perimeter += 1
            if (i == 0):
                perimeter += 1

            if (grid[i + 1][j] == 0 and i != len(grid) - 1 ):
                perimeter += 1
            if (i == len(grid) - 1):
                perimeter += 1

    return (perimeter)