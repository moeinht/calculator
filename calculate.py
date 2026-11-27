from operations import operations


def parse_ans(value, last_calculation):
    if value.lower() == "ans":
        if last_calculation is None:
            raise ValueError("No previous calculation!")
        return last_calculation

    return float(value)


def calculation(num1, num2, operation, last_calculation):
    if operation not in operations:
        raise ValueError("Invalid operation")

    num1 = parse_ans(num1, last_calculation)
    num2 = parse_ans(num2, last_calculation)

    result = operations[operation](num1, num2)

    return result
