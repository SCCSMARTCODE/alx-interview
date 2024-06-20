#!/usr/bin/python3
"""
This is the main module that runs the pascal code
"""


def pascal_triangle(n):
    """
    working on pascal...
    """
    if type(n) != int:
        return
    if n <= 0:
        return []

    result_rows = []
    park2 = [1]

    for row in range(n):
        if row != 0:
            park1 = park2
            new_park = [1, 1]
            if len(park1) == 1:
                park2.append(1)
            else:
                for x in range(1, len(park1)):
                    park2 = new_park
                    park2.insert(x, int(park1[x - 1]) + int(park1[x]))
        result_rows.append(park2[:])
    return result_rows
