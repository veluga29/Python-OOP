# 다른 클래스의 일부 메서드를 사용하고 싶지만, 상속은 하고 싶지 않을 때 사용
# 아래 사항을 피하기 위해 사용한다!
# 1. 부모 클래스가 변하면 자식 클래스는 계속 수정되어야 함
# 2. 부모 클래스의 메서드를 오버라이딩 하는 경우 내부 구현 방식의 얕은 이해로 오류가 생길 가능성 증가


class AI:
    def __init__(self, name, code):
        self.name = name
        self.code = code

    def cal_add(self, x, y):
        return x + y


class SiriCal:
    def __init__(self, name, code):
        self.AI = AI(name, code)

    def cal_add(self, x, y):
        return self.AI.cal_add(x, y)
