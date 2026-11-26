operations ={
    "+" : lambda x,y: x+y,
    "-": lambda x,y: x-y,
    "/": lambda x,y: x/y,
    "*": lambda x,y: x*y,
    "**": lambda x,y: x**y,
    "%": lambda x,y: x%y
}

last_calculation = None

def parse_ans(value, last_calculation):
    if value.lower() == 'ans':
        if last_calculation is None:
            raise ValueError("No previous calculation!")
        return last_calculation
    
    return float(value)


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

        num1 = parse_ans(num1 , last_calculation)
        num2 = parse_ans(num1 , last_calculation)

        result = operations[operation](num1, num2)

        last_calculation = result

        print(result)

    except ValueError:
        print("Input error: Invalid number")

    except ZeroDivisionError:
        print("Math error: Cannot divide by zero")