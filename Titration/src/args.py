from argparse import ArgumentParser, ArgumentTypeError
from typing import List


def parse_args() -> List[List[float]]:
    parser = ArgumentParser(usage="%(prog)s file")
    i: int = 0

    parser.add_argument(
        "file",
        type=str,
        help='a csv file containing "vol;ph" lines',
    )
    try:
        args = parser.parse_args()
    except SystemExit:
        exit(84)
    file = args.file
    file = file.split(".")
    if len(file) != 2 or file[1] != "csv":
        print("Invalide file, it must be a .csv")
        exit(84)
    try:
        f = open(args.file)
    except FileNotFoundError:
        print(f"No such file or directory: '{args.file}'")
        exit(84)
    values: List[str] = f.read().split("\n")
    rt: List[List[float]] = [[0]]
    for s in values:
        rt.append(s.split(";"))
    rt.pop(0)
    rt.remove([""])
    if len(rt) < 1:
        print("Empty file")
        exit(84)
    for i in rt:
        if len(i) != 2:
            print("Invalid args in file, must be pair args")
            exit(84)
        try:
            i[0] = float(i[0])
            i[1] = float(i[1])
        except ValueError:
            print("Invalid args in file, must be floats")
            exit(84)
    return rt
