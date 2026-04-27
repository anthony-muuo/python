
def add(n1, n2):
    return n1 + n2

def subtract (n1, n2):
    return n1 - n2

def multiply (n1, n2):
    return n1 * n2

def divide (n1, n2):
    return n1 / n2

# add the fns as the values in a dictionary
operations_dictonary = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
should_run_app = True

while should_run_app:
    first_number = float(input("Type the first number?: "))
    should_accumulate = True

    while should_accumulate:
        for symbol in operations_dictonary:
            print(symbol)

        maths_operation = input("Type a mathematical operation to do? ")
        second_number = float(input("Enter the second number "))
        answer = operations_dictonary[maths_operation](first_number, second_number)

        print(f"{first_number} {maths_operation} {second_number} = {answer}")

        choice = input(f"Type 'y' if you want to continue with {answer} or type 'n' to start a new calculation or 'quit' to stop the calc: ")

        if choice == 'y':
            first_number = answer
        elif choice == 'n':
            # break the inner loop
            should_accumulate = False
            # clear the screen and then restart by askin the first num
            print("\n" * 20)
        else:
            should_accumulate = False
            should_run_app = False
            print("GoodBye!!") 