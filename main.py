operations ={
    "+" : lambda x,y: x+y,
    "-": lambda x,y: x-y,
    "/": lambda x,y: x/y,
    "*": lambda x,y: x*y,
    "**": lambda x,y: x**y,
    "%": lambda x,y: x%y
}


def parse_ans(value, last_calculation):
    if value.lower() == 'ans':
        if last_calculation is None:
            raise ValueError("No previous calculation!")
        return last_calculation
    
    return float(value)

def calculation(num1,num2 ,operation,last_calculation):
    if operation not in operations:
        raise ValueError("Invalid operation")

    num1 = parse_ans(num1 , last_calculation)
    num2 = parse_ans(num2, last_calculation)

    result = operations[operation](num1, num2)

    return result



def get_numbers():
    actions = ('exit', 'history', 'clear', 'undo') 
    num1 = input(f"Enter first number {' / '.join(actions)} : ").strip()

    if num1.lower() in actions:
        return num1.lower()
    
    
    operation = input("Enter operation (+, -, /, *, %, **): ").strip()
    num2 = input("Enter second number: ").strip()

    if not num1 or not num2 or not operation:
        raise ValueError("Please enter all values!\n")

    return num1 , num2, operation


def show_histories(histories):
    if not histories:
        print("\nHistory is empty!\n")
        return

    print("\n----- History -----\n")

    for i, history in enumerate(histories, start=1):
        print(
            f"{i}. {history['num1']} "
            f"{history['operation']} "
            f"{history['num2']} = {history['result']}"
        )

    print("\n----- End -----\n")

def main():
    last_calculation = None
    histories = []

    while True:

        try:

            inputs = get_numbers()        
        
            if inputs == 'exit':
                print("Goodbye!")
                break

            if inputs == 'history':
                show_histories(histories)
                continue

            if inputs == 'clear':
                last_calculation = None
                histories.clear()
                print("\nHistory cleared!\n")
                continue

            if inputs == 'undo':
                if histories:
                    histories.pop()

                    if histories:
                        last_calculation = histories[-1]['result']
                    else:
                        last_calculation = None

                    print("Last calculation undone!\n")
                else:
                    print("\nThese is no history to undo it!\n")

                continue

            num1 ,num2 ,operation = inputs
            
            result = calculation(num1,num2 , operation, last_calculation)

            last_calculation = result 
            histories.append({"num1": num1 , "num2": num2 , 'operation' : operation, 'result': result})

            print(result)
            
        except ValueError as e:
            print(f"Error:{e}")

        except ZeroDivisionError:
            print("Math error: Cannot divide by zero")


if __name__ == '__main__':
    main()