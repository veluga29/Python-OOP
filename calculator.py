class Calculator:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        return self.x + self.y

    def subtract(self):
        return self.x - self.y

    def multiply(self):
        return self.x * self.y

    def devide(self):
        return self.x / self.y


cal1 = Calculator(1, 2)

print(cal1.add())
print(cal1.subtract())
cal1.x = 10
print(cal1.subtract())
