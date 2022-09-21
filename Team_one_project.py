# Program make a simple calculator

# This function adds two numbers
def add(x, y):
    return x + y


# This function subtracts two numbers
def subtract(x, y):
    return x - y


# This function multiplies two numbers
def multiply(x, y):
    return x * y


# This function divides two numbers
def divide(x, y):
    return x / y


# This function returns the remaining numbers by dividing the first number from the second.
def modulus(x, y):
    return x % y


# This function raise the first number to the power of the second number.
def exponentiation(x, y):
    return x ** y


# This function divide the first argument by the second and round the result down to the nearest whole number, making it equivalent to the math.floor () function.
def floor_division(x, y):
    return x // y


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.modulus")
print("6.exponentiation")
print("7.floor_division")


while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4/5/6/7): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4', '5', '6', '7'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))

        elif choice == '5':
            print(num1, "%", num2, "=", modulus(num1, num2))

        elif choice == '6':
            print(num1, "**", num2, "=",	exponentiation(num1, num2))


        elif choice == '7':
            print(num1, "//", num2, "=", floor_division(num1, num2))

        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
            break

    else:
        print("Invalid Input")
