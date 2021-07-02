from typing import NamedTuple, Union

GrowthRate = float


class Generations(NamedTuple):
    i0: int
    i1: int


class Bombyx(NamedTuple):
    n: int
    request: Union[GrowthRate, Generations]


def growth_rate(bombyx: Bombyx) -> None:
    if isinstance(bombyx.request, GrowthRate):
        k: float = bombyx.request
        n: float = bombyx.n

        for i in range(0, 100):
            print(f"{i + 1} {n:.2f}")
            n = k * n * ((1000 - n) / 1000)


def generations(bombyx: Bombyx) -> None:
    k: float = 1
    if isinstance(bombyx.request, Generations):
        i0: float = bombyx.request.i0
        i1: float = bombyx.request.i1
        x: float = bombyx.n
        while k <= 4:
            for n in range(0, int(i1) + 1):
                x = k * x * ((1000 - x) / 1000)
                if n >= i0:
                    print(f"{k:.2f} {round(x, 2):.2f}")
            k = k + 0.01
            x = bombyx.n


def main(bombyx: Bombyx) -> int:
    if isinstance(bombyx.request, GrowthRate):
        growth_rate(bombyx)
    if isinstance(bombyx.request, Generations):
        generations(bombyx)
    return 0
