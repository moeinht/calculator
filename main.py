def calculator(num1, operation, num2):
    if operation == '+':
        return num1 + num2

    elif operation == '-':
        return num1 - num2

    elif operation == '*':
        return num1 * num2

    elif operation == '/':
        if num2 == 0:
            raise ZeroDivisionError("Cannot divide by zero!")
        return num1 / num2

    elif operation == '%':
        if num2 == 0:
            raise ZeroDivisionError("Cannot modulo by zero!")
        return num1 % num2

    elif operation == '**':
        return num1 ** num2

    else:
        raise ValueError("Invalid operator!")


last_calculation = 0

while True:
    num1 = input("Enter first number (exit): ").strip()

    if num1.lower() == 'exit':
        print("Goodbye!")
        break

    operation = input("Enter operation (+, -, /, *, %, **): ").strip()
    num2 = input("Enter second number: ").strip()

    if not num1 or not num2 or not operation:
        print("Please enter all values!\n")
        continue

    try:
        if num1 == 'ans':
            num1 = last_calculation
        else:
            num1 = float(num1)
        num2 = float(num2)

        result = calculator(num1, operation, num2)

        last_calculation = result

        print(f"\n{num1} {operation} {num2} = {result}\n")

    except ValueError as e:
        print(f"Input error: {e}")

    except ZeroDivisionError as e:
        print(f"Math error: {e}")