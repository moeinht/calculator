def get_numbers():
    actions = ("exit", "history", "clear", "undo")
    num1 = input(f"Enter first number {' / '.join(actions)} : ").strip()

    if num1.lower() in actions:
        return num1.lower()

    operation = input("Enter operation (+, -, /, *, %, **): ").strip()
    num2 = input("Enter second number: ").strip()

    if not num1 or not num2 or not operation:
        raise ValueError("Please enter all values!\n")

    return num1, num2, operation
