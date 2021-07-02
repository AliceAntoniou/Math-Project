from argparse import ArgumentParser, ArgumentTypeError
from sys import argv
from typing import List, Tuple


def float_list_type(arg: str) -> List[float]:
    try:
        float_list = [float(i) for i in arg.split("*")]
    except ValueError:
        raise ArgumentTypeError(f"[{arg}] isn't a list of float")
    return float_list


def parse_args() -> List[List[float]]:
    parser = ArgumentParser(usage="%(prog)s [num den]*")
    parser.add_argument(
        "polynoms",
        metavar="num and den",
        nargs="+",
        type=float_list_type,
        help="polynoms",
    )
    polynoms: List[List[float]] = parser.parse_args().polynoms
    if len(polynoms) % 2 != 0:
        exit(84)
    return polynoms
