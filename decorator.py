def milk(func):
    def wrapper():
        print("milk")
        func()

    return wrapper


def espresso(func):
    def wrapper():
        print("espresso")
        func()

    return wrapper


def cup(func):
    def wrapper():
        func()
        print("\\______/")

    return wrapper


@milk
@espresso
@cup
def vanila():
    print("Vanila")


@milk
@espresso
@cup
def hazelnut():
    print("Hazelnut")


@milk
@espresso
@cup
def strawberry():
    print("Strawberry")


@milk
@espresso
@cup
def chocolate():
    print("Chocolate")


@milk
@espresso
@cup
def matcha():
    print("Matcha")


vanila()
hazelnut()
strawberry()
chocolate()
matcha()
