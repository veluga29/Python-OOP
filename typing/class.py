class WelshCorgi:
    def bark(self):
        return "woof! woof!"


wc = WelshCorgi()


def foo(ins: WelshCorgi) -> str:
    return ins.bark()


print(foo(wc))
