int_var: int = 128
str_var: str = "Welsh Corgi"
float_var: float = 3.14
bool_var: bool = True

list_var: list[str] = ["Welsh Corgi", "Poodle", "Pug"]
tuple_var: tuple[str, ...] = ("Welsh Corgi", "Poodle", "Pug")
tuple_var2: tuple[int, str, bool] = (1, "Welsh Corgi", True)

dic_var: dict[str, int] = {"Welsh Corgi": 1, "Poodle": 2, "Pug": 3}


def type_check(obj, typer) -> None:
    if isinstance(obj, typer):
        pass
    else:
        raise TypeError(f"Type Error : {typer}")


def cal_add(x: int, y: int) -> int:
    type_check(x, int)
    type_check(y, int)

    return x + y


print(cal_add(1, 2))
