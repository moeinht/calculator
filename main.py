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
    num1 = input("Enter first number (exit / history / clear): ").strip()

    if num1.lower() in ('exit', 'history', 'clear'):
        return num1.lower()
    
    
    operation = input("Enter operation (+, -, /, *, %, **): ").strip()
    num2 = input("Enter second number: ").strip()

    if not num1 or not num2 or not operation:
        raise ValueError("Please enter all values!\n")

    return num1 , num2, operation

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
                if len(histories) == 0:
                    print("\nHistory is empty!\n")
                else:
                    print("\n" + "-" * 5 + 'History', "-" * 5 + '\n')

                for i, history in enumerate(histories, start=1):
                    print(f"{i}. {history}")

                print("\n" + "-" * 5 + 'End', "-" * 5 + "\n")

                continue

            if inputs == 'clear':
                histories.clear()
                print("\nHistory cleared!\n")
                continue
        
            num1 ,num2 ,operation = inputs
            
            result = calculation(num1,num2 , operation, last_calculation)

            last_calculation = result 
            histories.append(f'{num1} {operation} {num2} = {result}')

            print(result)
            
        except ValueError as e:
            print(f"Error:{e}")

        except ZeroDivisionError:
            print("Math error: Cannot divide by zero")


if __name__ == '__main__':
    main()