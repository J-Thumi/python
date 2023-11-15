class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, x, y):
        self.result = x + y

def main():
    try:
        calculator = Calculator()

        x = float(input("Enter the first number: "))
        y = float(input("Enter the second number: "))

        calculator.add(x, y)

        result = calculator.result

        print(f"Result: {result}")

    except ValueError as ve:
        print(f"Error: Invalid input. Please enter valid numbers. {ve}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
