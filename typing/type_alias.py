from typing import Union, Optional
from typing_extensions import TypedDict

# type alias
Value = Union[
    int, bool, Union[list[str], tuple[str, ...], Optional[dict[int, bool]]]
]

value: Value = 17

A = int

a: A = 1


# JSON 형식의 데이터를 타이핑에 좋은 방법 - TypedDict (dict alias)
class Person(TypedDict):
    name: str
    age: int
    address: str


person: Person = {"name": "lugaluga", "age": 20, "address": "Seoul"}
