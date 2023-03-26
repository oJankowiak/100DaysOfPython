#Calculator

from replit import clear
from art import logo


# adding
def add(n1, n2):
    return n1 + n2
# subtraction
def subtract(n1, n2):
    return n1 - n2
# multiplication 
def multiply(n1, n2):
    return n1 * n2
# division
def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add, 
    "-": subtract,
    "*": multiply, 
    "/": divide
}

def calculator(): 
    print(logo)
    should_continue = True

    num1 = float(input("What's the first number?: "))
    for symbol in operations:
      print(symbol)

    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))

        calculation_result = operations[operation_symbol]
        answer = calculation_result(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") 
        if choice == 'y':
            num1 = answer
        else:
            should_continue = False
            clear()
            calculator()
calculator()