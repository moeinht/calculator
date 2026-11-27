from calculate import calculation
from history import show_histories
from input_handler import get_numbers


def main():
    last_calculation = None
    histories = []

    while True:
        try:
            inputs = get_numbers()

            if inputs == "exit":
                print("Goodbye!")
                break

            if inputs == "history":
                show_histories(histories)
                continue

            if inputs == "clear":
                last_calculation = None
                histories.clear()
                print("\nHistory cleared!\n")
                continue

            if inputs == "undo":
                if histories:
                    histories.pop()

                    if histories:
                        last_calculation = histories[-1]["result"]
                    else:
                        last_calculation = None

                    print("\nLast calculation undone!\n")
                else:
                    print("\nThese is no history to undo it!\n")

                continue

            num1, num2, operation = inputs

            result = calculation(num1, num2, operation, last_calculation)

            last_calculation = result
            histories.append(
                {"num1": num1, "num2": num2, "operation": operation, "result": result}
            )

            print(result)

        except ValueError as e:
            print(f"Error:{e}")

        except ZeroDivisionError:
            print("Math error: Cannot divide by zero")


if __name__ == "__main__":
    main()
