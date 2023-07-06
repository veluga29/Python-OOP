class SelfTest:
    name = "testtesttest"

    def __init__(self, x):
        self.x = x

    @classmethod
    def func1(cls):
        print(f"cls: {cls}")
        print("func1")

    def func2(self):
        print(f"self: {self}")
        print(f"class 내 self 주소: {id(self)}")
        print("func2")


test = SelfTest(1)


test.func2()
print(f"인스턴스의 주소: {id(test)}")

"""
self: <__main__.SelfTest object at 0x10b55fd90>  # = 메모리 위치
class 내 self 주소: 4485152144
func2
인스턴스의 주소: 4485152144
cls: <class '__main__.SelfTest'>
func1
"""

test.func1()  # 클래스 메서드는 인스턴스에서도 호출 가능하다.
print(test.name)  # 인스턴스에서 클래스 변수에 접근 가능하다.
