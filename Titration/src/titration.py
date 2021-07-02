from typing import List
from math import sqrt


def pH(i: int) -> float:
    return values[i][1]


def V(i: int) -> float:
    return values[i][0]


def calc_derivative() -> List[float]:
    i: int = 1
    result: List[float] = [0]
    size: int = len(values) - 1
    calc_1: float = 0
    calc_2: float = 0

    while i < size:
        calc_1 = (pH(i) - pH(i - 1)) / (V(i) - V(i - 1))
        calc_1 *= (V(i + 1) - V(i)) / (V(i + 1) - V(i - 1))
        calc_2 = (pH(i + 1) - pH(i)) / (V(i + 1) - V(i))
        calc_2 *= (V(i) - V(i - 1)) / (V(i + 1) - V(i - 1))
        result.append(calc_1 + calc_2)
        i += 1
    result.pop(0)
    return result


def calc_second_derivative(derivative: List[float]) -> List[float]:
    i: int = 2
    j: int = 1
    result: List[float] = [0]
    size: int = len(derivative)
    calc_1: float = 0
    calc_2: float = 0

    while i < size:
        calc_1 = (derivative[j] - derivative[j - 1]) / (V(i) - V(i - 1))
        calc_1 *= (V(i + 1) - V(i)) / (V(i + 1) - V(i - 1))
        calc_2 = (derivative[j + 1] - derivative[j]) / (V(i + 1) - V(i))
        calc_2 *= (V(i) - V(i - 1)) / (V(i + 1) - V(i - 1))
        result.append(calc_1 + calc_2)
        i += 1
        j += 1
    result.pop(0)
    return result


def calc_second_derivative_estimated(
    second_derivative: List[float], A: int, B: int
) -> List[float]:
    y: float = V(A)
    x: float = second_derivative[A - 2]
    calc_1: float = (second_derivative[A - 2] - second_derivative[B - 2]) / (
        V(A) - (V(B))
    )
    calc_2: float = (
        V(A) * second_derivative[B - 2] - V(B) * second_derivative[A - 2]
    ) / (V(A) - V(B))
    result: List[float] = [0]

    while y < V(B):
        x = calc_1 * y + calc_2
        result.append(x)
        y += 0.1
    result.pop(0)
    return result


def get_equivalence_point(derivates: List[float]) -> float:
    i: int = 1
    test: float = 0
    rt: int = 0

    while i < len(derivates):
        if derivates[i] > test:
            test = derivates[i]
            rt = i + 1
        i += 1
    return rt


def get_real_equivalence_point(derivates: List[float]) -> float:
    i: int = 1
    test: float = 10
    rt: int = 0

    while i < len(derivates):
        if abs(derivates[i]) < test:
            test = abs(derivates[i])
            rt = i + 1
        i += 1
    return rt - 1


def main(doc: List[List[float]]) -> int:
    i: int = 1
    global values
    values = doc
    derivative: List[float] = calc_derivative()
    point: int = get_equivalence_point(derivative)
    second_derivative: List[float] = calc_second_derivative(derivative)
    second_derivative_estimated: List[float] = calc_second_derivative_estimated(
        second_derivative, point - 1, point
    )

    second_derivative_estimated.pop(len(second_derivative_estimated) - 1)
    second_derivative_estimated += calc_second_derivative_estimated(
        second_derivative, point, point + 1
    )
    real_point: float = V(point - 1) + 0.1 * get_real_equivalence_point(
        second_derivative_estimated
    )

    print("Derivative:")
    for deriv in derivative:
        print(f"{values[i][0]} ml -> {deriv:.2f}")
        i += 1
    print(f"\nEquivalence point at {V(point)} ml\n")
    i = 2
    print("Second derivative:")
    for deriv in second_derivative:
        print(f"{values[i][0]} ml -> {deriv:.2f}")
        i += 1
    i = V(point - 1)
    print("\nSecond derivative estimated:")
    for result in second_derivative_estimated:
        print(f"{i:.1f} ml -> {result:.2f}")
        i += 0.1
    print(f"\nEquivalence point at {real_point} ml")
    return 0
