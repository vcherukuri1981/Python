# Functionality:
# Program asks the user to type the first number.
# Program asks the user to type a mathematical operator (a choice of "+", "-", "*" or "/")
# Program asks the user to type the second number.
# Program works out the result based on the chosen mathematical operator.
# Program asks if the user wants to continue working with the previous result.
# If yes, program loops to use the previous result as the first number and then repeats the calculation process.
# If no, program asks the user for the fist number again and wipes all memory of previous calculations.

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

input("Welcome to the Calculator! Press Enter to continue...")
def calculator():
    
    should_continue = True
    n1 = float(input("Type the first number: "))
    while should_continue:

        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation: ")
        n2 = float(input("Type the second number: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(n1, n2)
        print(f"{n1} {operation_symbol} {n2} = {answer}")

        choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation or q to quit: ")
        if choice == 'y':
            n1 = answer
        elif choice == 'q':
            should_continue = False
        else:
            should_continue = False
            calculator()

calculator()