# 
""" Project - construct a calculator with basic functions """
#

# import logo
from calculator_art import logo

## Functions
# Addition
def add(n1, n2):
    return n1 + n2

# Subtraction
def subtract(n1, n2):
    return n1 - n2

# Multiplication
def multiply(n1, n2):
    return n1 * n2

# Division
def divide(n1, n2):
    return n1 / n2

# define dictionary with operations
operations_dictionary = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    print(logo)
    isRunning = True

    num1 = float(input("What's the first number?: "))
    for symbol in operations_dictionary:
            print(symbol) 

    while isRunning:
        operation_sign = input("What operation would you like to perform?: ")

        num2 = float(input("What's the second number?: "))

        calculation_function = operations_dictionary[operation_sign]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_sign} {num2} = {answer}")

        if input(f"Type y to continue calculating with {answer}, or type 'n' to start a new calculation: ") == "y":
            num1 = answer
        else:
            isRunning = False
            calculator()
        
calculator()