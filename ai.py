"""
- namespace: 개체를 구분할 수 있는 범위
- __dict__: 클래스나 인스턴스의 namespace를 dictionary 형태로 반환
- dir(): 네임스페이스의 key값을 확인할 수 있다.
- __doc__: 클래스의 독스트링을 확인한다
- __class__: 어떤 클래스로 만들어진 인스턴스인지 확인할 수 있다.
"""


class AI:
    # 클래스 변수
    population = 0

    # 생성자 함수
    def __init__(self, name):
        self.name = name  # 인스턴스 변수
        AI.population += 1

    # 인스턴스 메서드
    def cook(self):
        print(f"{self.name} is cooking!")

    def clean(self):
        print(f"{self.name} is cleaning!")

    def switchoff(self):
        print(f"{self.name} is switched off!")
        AI.population -= 1

    # 클래스 메서드
    @classmethod
    def how_many(cls):
        print(f"AI population is {cls.population}.")

    # Static 메서드
    @staticmethod
    def hello():
        print("Hello!")


bixby = AI("Bixby")
siri = AI("Siri")

AI.how_many()

ga = AI("Google Assistant")

AI.how_many()

bixby.switchoff()

AI.how_many()

AI.hello()

print(AI.__dict__)
# 인스턴스의 네임스페이스에 없는 키값에 접근하면 해당 인스턴스의 클래스 네임스페이스로 접근한다.
print(bixby.__dict__)
print(dir(AI))
print(dir(bixby))
