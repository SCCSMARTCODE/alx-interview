#!/usr/bin/python3
"""
This module contains the solution to the island perimeter problem
"""


def island_perimeter(grid):
    """
    :param grid:
    :return:
    """
    perimeter = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 1:
                perimeter += 4
                check_points = [(row + 1, col), (row - 1, col),
                                (row, col + 1), (row, col - 1)]
                for point in check_points:
                    try:
                        if -1 in point:
                            continue
                        if grid[point[0]][point[1]] == 1:
                            perimeter -= 1
                    except IndexError:
                        continue
    return perimeter
