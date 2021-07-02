from typing import List
from math import sqrt
from src.types import Matrix, Trigo
from src.matrix import get_identity_matrix
from src.functions import my_exp, my_cos, my_sin, my_cosh, my_sinh


def print_result(result: Matrix) -> None:
    vec = len(result)

    for i in range(vec):
        for k in range(vec):
            print(f"{result[i][k]:.2f}", end="")
            if k + 1 == vec:
                print("\n", end="")
            else:
                print("\t", end="")
        k = 0


def main(args: Trigo) -> int:
    vec = len(args.matrix)
    result: Matrix = [[0.0 for x in range(vec)] for y in range(vec)]
    if args.function == "EXP":
        result = my_exp(args.matrix)
    if args.function == "COS":
        result = my_cos(args.matrix)
    if args.function == "SIN":
        result = my_sin(args.matrix)
    if args.function == "COSH":
        result = my_cosh(args.matrix)
    if args.function == "SINH":
        result = my_sinh(args.matrix)
    print_result(result)
    return 0
