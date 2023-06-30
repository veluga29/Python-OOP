"""
#* [property]
#* 인스턴스 변수 값을 사용해서 적절한 값으로 보내고 싶을 때
#* 인스턴스 변수 값에 대한 유효성 검사 및 수정
"""


class AI:
    __population = 0

    def __init__(self, name, code):
        self.__name = name
        self.__code = code  # private
        AI.__population += 1

    @property
    def name(self):
        return f"Housekeeper: {self.__name}"

    @property
    def code(self):
        return self.__code

    @code.setter
    def code(self, new_code):
        if len(str(new_code)) == 12:
            self.__code = new_code
        else:
            raise ValueError("Invalid code!")

    def hello(self):
        print(f"Hello! I'm {self.name}")

    def cal_add(self, x, y):
        return x + y

    @classmethod
    def how_many(cls):
        print(f"We have {cls.__population} AIs.")


ai = AI("Hasty", 980812048109)
print(ai.name)
print(ai.code)

ai.code = 123456789012

print(ai.code)
