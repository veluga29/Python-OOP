# 데이터 형식에 의존하지 않고, 하나의 값이 여러 다른 데이터 타입들을 가질 수 있는 기술
from typing import TypeVar, Generic

T = TypeVar("T", str, int)
A = TypeVar("A", int, bool)


class Dog(Generic[T, A]):
    def __init__(self, leg: T, tail: A):
        self.leg: T = leg
        self.tail: A = tail


dog1 = Dog[int, bool](leg=4, tail=False)
dog2 = Dog[str, bool](leg="four", tail=True)
dog3 = Dog[int, int](leg=4, tail=9)

# This is allowed, too
# dog1 = Dog(leg=4, tail=False)
# dog2 = Dog(leg="four", tail=True)
# dog3 = Dog(leg=4, tail=9)


class WelshCorgi(Generic[T, A], Dog[T, A]):
    pass


wc1 = WelshCorgi[int, bool](leg=4, tail=False)
wc2 = WelshCorgi[str, bool](leg="four", tail=True)
wc3 = WelshCorgi[int, int](leg=4, tail=9)


print(wc1.leg)


# function
def foo(x: T) -> T:
    return x


print(foo("woof!"))
print(foo(1))
