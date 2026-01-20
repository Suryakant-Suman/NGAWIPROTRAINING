
class Calculator:
    def calculate(self, a, b):
        return a + b

class AdvancedCalculator(Calculator):
    def calculate(self, a, b):
        return a * b

class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return Number(self.value + other.value)

    def __str__(self):
        return str(self.value)

calc = Calculator()
adv_calc = AdvancedCalculator()

print("Calculator Result:", calc.calculate(10, 5))
print("AdvancedCalculator Result:", adv_calc.calculate(10, 5))

n1 = Number(20)
n2 = Number(30)
n3 = n1 + n2

print("Operator Overloading Result:", n3)

for obj in (calc, adv_calc):
    print("Polymorphic Call:", obj.calculate(4, 3))
