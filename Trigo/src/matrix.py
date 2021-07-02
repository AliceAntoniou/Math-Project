from typing import List
from math import sqrt
from copy import deepcopy
from src.types import Matrix


def create_matrix(coef_list: List[int]) -> Matrix:
    vector = int(sqrt(len(coef_list)))
    matrix: Matrix = [[0.0 for x in range(vector)] for y in range(vector)]

    i = 0
    x = 0
    y = 0
    while i < len(coef_list):
        while x < vector:
            matrix[y][x] = coef_list[i]
            x += 1
            i += 1
        x = 0
        y += 1
    return matrix


def matrix_comparison(matrix1: Matrix, matrix2: Matrix) -> int:
    if len(matrix1) != len(matrix2):
        return 1

    vec = len(matrix1)
    for i in range(0, vec):
        for k in range(0, vec):
            if not (-0.01 < matrix1[i][k] - matrix2[i][k] < 0.01):
                return 1
    return 0


def get_identity_matrix(vec: int) -> Matrix:
    matrix: Matrix = [[0.0 for x in range(vec)] for y in range(vec)]

    for i in range(vec):
        matrix[i][i] = 1
    return matrix


def square_n_matrix(matrix: Matrix, n: int) -> Matrix:
    vec = len(matrix)
    final: Matrix = [[0.0 for x in range(vec)] for y in range(vec)]
    tmp: Matrix = deepcopy(matrix)
    y_tmp: int = 0
    x_tmp: int = 0
    y_matrix: int = 0
    x_matrix: int = 0

    if n == 0:
        return get_identity_matrix(vec)
    elif n == 1:
        return deepcopy(matrix)
    for i in range(1, n):
        final = [[0.0 for x in range(vec)] for y in range(vec)]
        for y_result in range(0, vec):
            for x_result in range(0, vec):
                for j in range(0, vec):
                    final[y_result][x_result] += (
                        tmp[y_tmp][x_tmp] * matrix[y_matrix][x_matrix]
                    )
                    x_tmp += 1
                    y_matrix += 1
                x_matrix += 1
                x_tmp = 0
                y_matrix = 0
            y_tmp += 1
            x_matrix = 0
        tmp = final
        y_tmp = 0
    return final


def mult_matrix_by_x(matrix: Matrix, i: float) -> Matrix:
    vec = len(matrix)

    for y in range(0, vec):
        for x in range(0, vec):
            matrix[y][x] *= i
    return deepcopy(matrix)


def div_matrix_by_x(matrix: Matrix, i: float) -> Matrix:
    vec = len(matrix)

    for y in range(0, vec):
        for x in range(0, vec):
            if i == 0:
                print("Error: Division by zero")
                exit(84)
            matrix[y][x] /= i
    return deepcopy(matrix)


def add_matrix(matrix1: Matrix, matrix2: Matrix) -> Matrix:
    vec = len(matrix1)
    for y in range(vec):
        for x in range(vec):
            matrix1[y][x] += matrix2[y][x]
    return deepcopy(matrix1)
