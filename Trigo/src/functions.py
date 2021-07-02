from src.types import Matrix
from src.matrix import (
    matrix_comparison,
    square_n_matrix,
    get_identity_matrix,
    mult_matrix_by_x,
    div_matrix_by_x,
    add_matrix,
)
from math import factorial
from copy import deepcopy

def my_exp(matrix: Matrix) -> Matrix:
    vec = len(matrix)
    result: Matrix = get_identity_matrix(vec)
    save: Matrix = [[0.0 for x in range(vec)] for y in range(vec)]
    tmp: Matrix = deepcopy(save)
    i = 0

    while matrix_comparison(result, save) != 0:
        save = deepcopy(tmp)
        matrix_power = square_n_matrix(matrix, i)
        matrix_divised = div_matrix_by_x(matrix_power, factorial(i))
        result = add_matrix(matrix_divised, save)
        tmp = deepcopy(result)
        i += 1
    return result


def my_cos(matrix: Matrix) -> Matrix:
    vec = len(matrix)
    result: Matrix = get_identity_matrix(vec)
    save: Matrix = [[0.0 for x in range(vec)] for y in range(vec)]
    tmp: Matrix = deepcopy(save)
    i = 0

    while matrix_comparison(result, save) != 0:
        save = deepcopy(tmp)
        matrix_power = square_n_matrix(matrix, 2 * i)
        matrix_divised = div_matrix_by_x(
            mult_matrix_by_x(matrix_power, (-1) ** i), factorial(2 * i)
        )
        result = add_matrix(matrix_divised, save)
        tmp = deepcopy(result)
        i += 1
    return result


def my_sin(matrix: Matrix) -> Matrix:
    vec = len(matrix)
    result: Matrix = get_identity_matrix(vec)
    save: Matrix = [[0.0 for x in range(vec)] for y in range(vec)]
    tmp: Matrix = deepcopy(save)
    i = 0

    while matrix_comparison(result, save) != 0:
        save = deepcopy(tmp)
        matrix_power = square_n_matrix(matrix, 2 * i + 1)
        matrix_divised = div_matrix_by_x(
            mult_matrix_by_x(matrix_power, (-1) ** i), factorial(2 * i + 1)
        )
        result = add_matrix(matrix_divised, save)
        tmp = deepcopy(result)
        i += 1
    return result


def my_cosh(matrix: Matrix) -> Matrix:
    vec = len(matrix)
    result: Matrix = get_identity_matrix(vec)
    save: Matrix = [[0.0 for x in range(vec)] for y in range(vec)]
    tmp: Matrix = deepcopy(save)
    i = 0

    while matrix_comparison(result, save) != 0:
        save = deepcopy(tmp)
        matrix_power = square_n_matrix(matrix, 2 * i)
        matrix_divised = div_matrix_by_x(matrix_power, factorial(2 * i))
        result = add_matrix(matrix_divised, save)
        tmp = deepcopy(result)
        i += 1
    return result


def my_sinh(matrix: Matrix) -> Matrix:
    vec = len(matrix)
    result: Matrix = get_identity_matrix(vec)
    save: Matrix = [[0.0 for x in range(vec)] for y in range(vec)]
    tmp: Matrix = deepcopy(save)
    i = 0

    while matrix_comparison(result, save) != 0:
        save = deepcopy(tmp)
        matrix_power = square_n_matrix(matrix, 2 * i + 1)
        matrix_divised = div_matrix_by_x(matrix_power, factorial(2 * i + 1))
        result = add_matrix(matrix_divised, save)
        tmp = deepcopy(result)
        i += 1
    return result
