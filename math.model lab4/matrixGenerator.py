import math
import random

import numpy


def generate_matrix(n, k):
    matrix = numpy.zeros((n, n), dtype=numpy.float_)
    values = [0, -1, -2, -3, -4]

    for i in range(n):
        for j in range(n):
            if i != j:
                matrix[i][j] = values[random.randint(0, 4)]

    matrix[0][0] = -sum(matrix[0]) + math.pow(10, -k)

    for i in range(1, n):
        matrix[i][i] = -sum(matrix[i])

    return matrix


def put_k_in_matrix(k, matrix):
    matrix[0][0] = 0
    matrix[0][0] = -sum(matrix[0]) + math.pow(10, -k)


def generate_hilbert_matrix(n):
    matrix = numpy.zeros((n, n), dtype=numpy.float_)
    for i in range(n):
        for j in range(n):
            matrix[i][j] = 1 / float(i + j + 1)

    return matrix


def generate_additional_matrix(n):
    matrix = []
    for i in range(n):
        matrix.append([i + 1])

    return matrix


