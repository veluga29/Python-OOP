import timeit


class WithoutSlotClass:
    def __init__(self, name, code):
        self.name = name
        self.code = code


wos = WithoutSlotClass("veluga", 20)

print(wos.__dict__)


class WithSlotClass:
    __slots__ = ["name", "code"]

    def __init__(self, name, code):
        self.name = name
        self.code = code


ws = WithSlotClass("veluga", 20)

print(ws.__slots__)


# Compare memory usage
def repeat(obj):
    def inner():
        obj.name = "veluga"
        obj.code = 20
        del obj.name
        del obj.code

    return inner


use_slot_time = timeit.repeat(repeat(ws), number=9999999)
no_slot_time = timeit.repeat(repeat(wos), number=9999999)


print("use slot : ", min(use_slot_time))
print("no slot : ", min(no_slot_time))
