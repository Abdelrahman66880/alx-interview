#!/usr/bin/python3
"""A script to rotate a 2D matrix anti-clockwise in-place.
"""


def transpose(matrix):
    """Transpose the matrix in-place using the zip function."""
    for i, row in enumerate(zip(*matrix)):
        matrix[i][:] = row


def reverse(matrix):
    """Reverse each row of the matrix in-place."""
    for row in matrix:
        row.reverse()


def rotate_2d_matrix(matrix):
    """Rotate the 2D matrix anti-clockwise in-place."""
    transpose(matrix)
    reverse(matrix)
