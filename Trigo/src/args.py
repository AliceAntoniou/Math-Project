from src.types import Trigo, Matrix
from src.matrix import create_matrix
from argparse import ArgumentParser, ArgumentTypeError
from typing import List
from math import sqrt


def trigo_fct(fct: str) -> str:
    allowed_fct: List[str] = ["EXP", "COS", "SIN", "COSH", "SINH"]
    if not fct in allowed_fct:
        raise ArgumentTypeError
    return fct


def parse_args() -> Trigo:
    parser = ArgumentParser(usage="%(prog)s fun a0 a1 a2 ...")
    parser.add_argument(
        "fun",
        type=trigo_fct,
        help='function to be applied, among at least "EXP", "COS", "SIN", "COSH" and "SINH"',
    )
    parser.add_argument("ai", type=int, nargs="+", help="coefficients of the matrix")

    try:
        args = parser.parse_args()
    except SystemExit:
        exit(84)

    nb_coef: int = len(args.ai)
    if ((sqrt(nb_coef) * 10) % 10 != 0) or (nb_coef < 4):
        print("Error: Square matrix requested")
        exit(84)

    matrix: Matrix = create_matrix(args.ai)
    return Trigo(args.fun, matrix)
