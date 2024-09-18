# 1. The Calculator App

# seems like you could just use the shell for this, but whatever
def addition():
    first_number = float(input("What is the first number you'd like to add? "))
    second_number = float(input("What is the second number you'd like to add? "))
    result = first_number + second_number
    print("The answer is", result)

def subtraction():
    first_number = float(input("What is the first number? "))
    second_number = float(input("And what would you like to subtract from that? "))
    result = first_number - second_number
    print("The answer is", result)


def multiplication():
    first_number = float(input("What is the first number you'd like to multiply? "))
    second_number = float(input("What is the second number you'd like to multiply? "))
    try:
        result = first_number * second_number
        print("The answer is", round(result, 2))
    except OverflowError:
        print("That's a very big number.")

def division():
    first_number = float(input("What is the first number you'd like to divide? "))
    second_number = float(input("And what would you like to divide that by? "))
    try:
        result = first_number / second_number
        print("The answer is", round(result, 2))
    except ZeroDivisionError:
        print("You can't divide by zero!")


which_operation = input("Would you like to do addition, subtraction, multiplication, or division? ")
which_operation = which_operation.lower()
if which_operation == "addition":
    addition()
elif which_operation == "subtraction":
    subtraction()
elif which_operation == "multiplication":
    multiplication()
elif which_operation == "division":
    division()
else:
    print("Not a valid input.")
print("Thanks for using my calculator program!")