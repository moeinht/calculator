operations ={
    "+" : lambda x,y: x+y,
    "-": lambda x,y: x-y,
    "/": lambda x,y: x/y,
    "*": lambda x,y: x*y,
    "**": lambda x,y: x**y,
    "%": lambda x,y: x%y
}

last_calculation = None

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
        if operation not in operations:
            print("Invalid operation")
            continue

        if num1.lower() == "ans":
            if last_calculation is None:
                print("No previous calculation!")
                continue
            num1 = last_calculation
        else:
            num1 = float(num1)

        num2 = float(num2)

        result = operations[operation](num1, num2)

        last_calculation = result

        print(result)

    except ValueError:
        print("Input error: Invalid number")

    except ZeroDivisionError:
        print("Math error: Cannot divide by zero")