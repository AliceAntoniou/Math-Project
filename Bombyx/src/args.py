from argparse import ArgumentParser, ArgumentTypeError
from .bombyx import Bombyx, Generations
from sys import argv


def positive_int(arg: str) -> int:
    try:
        value = int(arg)
    except ValueError:
        raise ArgumentTypeError(f"{arg} isn't a positive integer")

    if value <= 0:
        raise ArgumentTypeError(f"{arg} isn't a positive integer")

    return value


def rate(arg: str) -> float:
    try:
        value = float(arg)
    except ValueError:
        raise ArgumentTypeError(f"{arg} isn't a float between 1 and 4")

    if value <= 1 or value > 4:
        raise ArgumentTypeError(f"{value} isn't a float between 1 and 4")

    return value


def parse_args() -> Bombyx:
    parser = ArgumentParser(usage="%(prog)s n [k | i0 i1]")

    parser.add_argument(
        "initial_population",
        type=positive_int,
        help="number of first generation individuals",
    )
    parser.add_argument(
        "--growth_rate", metavar="k", type=rate, help="Growth rate from 1 to 4"
    )
    parser.add_argument(
        "--generations",
        metavar=("i0", "i1"),
        nargs=2,
        type=positive_int,
        help="Generations",
    )

    args = argv[1:]
    if len(args) == 2:
        args.insert(1, "--growth_rate")
    elif len(args) == 3:
        args.insert(1, "--generations")

    try:
        parsed_args = parser.parse_args(args)
    except SystemExit:
        exit(84)

    if not parsed_args.growth_rate is None:
        return Bombyx(parsed_args.initial_population, parsed_args.growth_rate)

    if not parsed_args.generations is None:
        generations = Generations(*parsed_args.generations)
        if generations.i0 > generations.i1:
            exit(84)
        return Bombyx(parsed_args.initial_population, generations)

    print("No action passed")
    exit(84)
