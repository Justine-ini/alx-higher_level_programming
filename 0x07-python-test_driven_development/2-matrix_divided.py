#!/usr/bin/python3
def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix.

    Args:
        matrix: A list of lists of integers or floats.
        div: A number (integer or float).

    Returns:
        A new matrix with all elements divided by div.
    """

    if not isinstance(matrix, list):
        raise TypeError('matrix must be a list of lists')

    for row in matrix:
        if not isinstance(row, list):
            raise TypeError('matrix must be a list of lists')

    if len(matrix[0]) != len(matrix[1]):
        raise TypeError('Each row of the matrix must have the same size')

    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')

    if div == 0:
        raise ZeroDivisionError('division by zero')

    new_matrix = []
    for row in matrix:
        new_row = [round(element / div, 2) for element in row]
        new_matrix.append(new_row)

    return new_matrix
