class AI:
    population = 0

    def __init__(self, name, code, color):
        self.name = name
        self.__code = code  # private
        # 유사 protected (개념적으로는 상속받은 대상에게만 오픈, but python에서는 public)
        self._color = color
        AI.population += 1

    def hello(self):
        print(f"Hello! I'm {self.name}")

    def cal_add(self, x, y):
        return x + y

    @classmethod
    def how_many(cls):
        print(f"We have {cls.population} AIs.")


class Bixby(AI):
    def __init__(self, name, code, color):
        super().__init__(name, code, color)

    def get_attributes(self):
        print(f"{self.name}'s color is {self._color}")


ai = AI("ai", 98081204810, "white")
bixby = Bixby("bixby", 84091267, "blue")
bixby.get_attributes()
print(bixby._color)
# print(ai.__code)  # error
# print(bixby.__code)  # error
