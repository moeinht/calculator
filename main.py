def calculator(num1, operation, num2):
    if operation == '+':
        return num1 + num2

    elif operation == '-':
        return num1 - num2

    elif operation == '*':
        return num1 * num2

    elif operation == '/':
        if num2 == 0:
            raise ZeroDivisionError()
        return num1 / num2
    
    elif operation == '**':
        return num1 ** num2
    
    else:
        raise ValueError("Please choose a valid operation!")


while True:
    num1 = input("Enter first number (exit): ").strip()

    if num1.lower() == 'exit':
        print("Goodbye!")
        break

    operation = input("Enter operation (+, -, /, *, **): ").strip()
    num2 = input("Enter second number: ").strip()

    if not num1 or not num2 or not operation:
        print("Please enter all values!\n")
        continue

    try:
        result = calculator(float(num1), operation, float(num2))
        print(f"\n{num1} {operation} {num2} = {result}\n")

    except ValueError:
        print("Invalid number or operation!")

    except ZeroDivisionError as e:
        print(f"Error: {e}")