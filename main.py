# create a calculator program using functions
print("Welcome to the calculator program")


def addition(num1, num2):
    return num1 + num2


def subtraction(num1, num2):
    return num1 - num2


def division(num1, num2):
    return num1 / num2


def multiplication(num1, num2):
    return num1 * num2


option = int(input("""
Pick an option:
1. Addition
2. Subtraction
3. Division
4. Multiplication
"""))

number1 = int(input("Enter a number: "))
number2 = int(input("Enter another number: "))

if option == 1:
    print(number1, "+", number2, "is equals to", addition(number1, number2))
elif option == 2:
    print(number1, "-", number2, "is equals to", subtraction(number1, number2))
elif option == 3:
    print(number1, "/", number2, "is equals to", division(number1, number2))
elif option == 4:
    print(number1, "*", number2, "is equals to", multiplication(number1, number2))
else:
    quit()
