#importing logo
from art import logo


#create function for add,sub,mul,div,mod
def add(number1,number2):
    """return addition of two numbers"""
    return number1 + number2

def subtract(number1,number2):
    """return subtraction of two numbers"""
    return number1 - number2

def multiply(number1,number2):
    """return multiplication of two numbers"""
    return number1 * number2

def divide(number1,number2):
    """return division of two numbers"""
    return number1 / number2

def mod(number1,number2):
    """return modulus of two numbers"""
    return number1 % number2

operations = {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide,
    "%":mod
}


def calculator():
    """main calculator function"""
    print(logo)
    inp_number1 = eval(input("Enter your 1st number: "))
    for symbol in operations:
        print(symbol,end="\t")

    while True:
        inp_operation = input("\nEnter a operation : ")
        inp_number2 = eval(input("Enter your next number: "))
        calculation = operations[inp_operation]
        result = calculation(inp_number1,inp_number2)
        print(f"{inp_number1} {inp_operation} {inp_number2} = {result}")

        choice = input(f"press 'y' to continue calculating with {result} ,'n' to exit and 's' to start fresh : ").lower()
        if choice == 'y' :
            inp_number1 = result
        elif choice == 's':
            calculator()
        else:
            exit()
calculator()
        





