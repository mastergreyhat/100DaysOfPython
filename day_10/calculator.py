import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def calculator(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 == 0:
            print("Error: Division by zero.")
            return None
        return num1 / num2
    else:
        return None

while True:
    num1 = float(input("What's the first number?: "))
    while True:
        print("+\n-\n*\n/")
        operation = input("Choose an operation: ")
        num2 = float(input("What's the next number?: "))
        result = calculator(num1, num2, operation)
        if result is None:
            print("Invalid Operation")
            exit()
        print(f"{num1} {operation} {num2} = {result}\n")
        proceed = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
        if proceed == 'y':
            num1 = result
        elif proceed == 'n':
            clear_screen()
            break
        else:
            print("Invalid input. Exiting.")
            exit()