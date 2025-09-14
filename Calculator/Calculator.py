def calculator(num1, operator, num2):
    """Simple calculator supporting +, -, *, /"""
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            return "Error! Division by zero."
        return num1 / num2
    else:
        return "Invalid operator"


if __name__ == "__main__":
    num1 = float(input("Enter first number: "))
    operator = input("Enter the operator (+, -, *, /): ")
    num2 = float(input("Enter second number: "))

    result = calculator(num1, operator, num2)
    print(f"Result: {result}")
