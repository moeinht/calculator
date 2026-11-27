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
    num1 = input("Enter first number (exit): ").strip()

    if num1.lower() == 'exit':
        print("Goodbye!")
        return None

    operation = input("Enter operation (+, -, /, *, %, **): ").strip()
    num2 = input("Enter second number: ").strip()

    if not num1 or not num2 or not operation:
        raise ValueError("Please enter all values!\n")

    return num1 , num2, operation

def main():
    last_calculation = None

    while True:

        try:

            inputs = get_numbers()        
        
            if inputs is None:
                break
        
            num1 ,num2 ,operation = inputs
            
            result = calculation(num1,num2 , operation, last_calculation)

            last_calculation = result 

            print(result)
            
        except ValueError as e:
            print(f"Error:{e}")

        except ZeroDivisionError:
            print("Math error: Cannot divide by zero")


if __name__ == '__main__':
    main()