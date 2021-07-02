from typing import List
from argparse import Namespace


def horner(polynom: List[float], x: float) -> float:
    n = len(polynom)
    value: float = polynom[n - 1]
    for i in range(n - 2, -1, -1):
        value = value * x + polynom[i]
    return value


def main(polynoms: List[List[float]]) -> int:
    x: float = 0
    length: int = len(polynoms)
    result: float = 1
    num: float = 0
    det: float = 0
    while round(x, 3) <= 1:
        result = 1
        for i in range(0, length, 2):
            num = horner(polynoms[i], x)
            det = horner(polynoms[i + 1], x)
            if det == 0:
                return 84
            result = result * (num / det)
        print(f"{x:.3f} -> {result:.5f}")
        x = x + 0.001
    return 0
