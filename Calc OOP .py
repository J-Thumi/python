class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, x, y):
        self.result = x + y

    def get_result(self):
        return self.result


calculator = Calculator()
x = float(input("Enter the first number: "))
y = float(input("Enter the second number: "))
calculator.add(x, y)

result = calculator.get_result()

print(f"Result: {result}")


