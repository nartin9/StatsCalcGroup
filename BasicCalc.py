import math


# adds two numbers
def add(x, y):
    return x + y


# subtracts two numbers
def subtract(x, y):
    return x - y


# multiplies two numbers
def multiply(x, y):
    return x * y


# divides two numbers
def divide(x, y):
    return x / y


# squares a number
def square(x):
    return x * x


# finds the square root of a number
def squareRoot(x):
    return math.sqrt(x)


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Square")
print("6.Square root")
choice = input("Enter choice(1/2/3/4/5/6): ")
num1 = float(input("Enter first number: "))
if choice == '1':
    num2 = float(input("Enter second number: "))
    print(num1, "+", num2, "=", add(num1, num2))
elif choice == '2':
    num2 = float(input("Enter second number: "))
    print(num1, "-", num2, "=", subtract(num1, num2))
elif choice == '3':
    num2 = float(input("Enter second number: "))
    print(num1, "*", num2, "=", multiply(num1, num2))
elif choice == '4':
    num2 = float(input("Enter second number: "))
    print(num1, "/", num2, "=", divide(num1, num2))
elif choice == '5':
    print(num1, " squared =", square(num1))
elif choice == '6':
    print(num1, " squared root =", squareRoot(num1))
else:
    print("Invalid input")
