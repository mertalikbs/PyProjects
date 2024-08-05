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
    # Normalde tırnağa alarak + işaretini stringe atayabilirdik ancak sadece add yazarak fonksiyona atadık.
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    def is_calculating():
        is_calculating = input("Do you want to continue calculator? 'y' for yes and 'n' for no. ")
        if is_calculating == "n":
            return False
        elif is_calculating == "y":
            return True
        else:
            print("You have entered an invalid command. The calculator ends itself.")
            return False
    
    num1 = int(input("What is the first number?  "))
    for symbol in operations:
        print(symbol)
    
    operation_symbol = input("Pick an operation from the line above:  ")
    num2 = int(input("What is the second number?  "))
    operation_function = operations[operation_symbol]
    result = operation_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {result}.")
    
    should_continue = is_calculating()
    while should_continue:
        operation_symbol2 = input("Pick an another operation from the symbols:  ")
        num3 = int(input("What is the other number?  "))
        operation_function = operations[operation_symbol2]
        result = operation_function(result, num3)
        print(result)
        should_continue = is_calculating()
    if should_continue == False:
        calculator()
calculator()
