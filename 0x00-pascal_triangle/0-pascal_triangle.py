#!/usr/bin/python3
'''A module for working with Pascal's triangle.

This module provides functionality to generate Pascal's triangle
up to a specified number of rows.

Functions:
- pascal_triangle(n): Generates Pascal's triangle up to n rows and returns it
  as a list of lists of integers.
'''


def pascal_triangle(n):
    '''Creates a list of lists of integers representing the Pascal's triangle
    of a given integer.

    Args:
    n (int): The number of rows to generate for Pascal's triangle.

    Returns:
    list: A list of lists of integers representing Pascal's triangle.
    '''
    triangle = []
    if type(n) is not int or n <= 0:
        return triangle

    for row_num in range(n):
        row = []
        for col_num in range(row_num + 1):
            if col_num == 0 or col_num == row_num:
                row.append(1)
            elif row_num > 0 and col_num > 0:
                row.append(triangle[row_num - 1][col_num -
                           1] + triangle[row_num - 1][col_num])
        triangle.append(row)

    return triangle
