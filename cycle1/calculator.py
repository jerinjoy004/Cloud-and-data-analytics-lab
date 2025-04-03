def calculator():
    print("Simple Calculator")
    print("Operations:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    while True:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            operation = input("Choose operation (+, -, *, /) or 'q' to quit: ")

            if operation == 'q':
                print("Exiting calculator...")
                break

            if operation == '+':
                result = num1 + num2
                print(f"Result: {num1} + {num2} = {result}")
            elif operation == '-':
                result = num1 - num2
                print(f"Result: {num1} - {num2} = {result}")
            elif operation == '*':
                result = num1 * num2
                print(f"Result: {num1} * {num2} = {result}")
            elif operation == '/':
                if num2 == 0:
                    print("Error: Division by zero!")
                else:
                    result = num1 / num2
                    print(f"Result: {num1} / {num2} = {result}")
            else:
                print("Invalid operation! Please try again.")

        except ValueError:
            print("Invalid input! Please enter numbers only.")


if __name__ == "__main__":
    calculator()
