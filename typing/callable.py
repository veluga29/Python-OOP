# Callable 객체(ex. 함수)의 typing

from typing import Callable


def add(x: int, y: int) -> int:
    return x + y


def bar(func: Callable[[int, int], int]) -> int:
    return func(10, 20)


print(bar(add))
