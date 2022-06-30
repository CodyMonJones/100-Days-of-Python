def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 // num2

num_1 = int(input("Enter the first number: "))
operation = input("What operation would you like to perform? +, -, *, /: ")
num_2 = int(input("Enter the second number: "))

if operation == "+":
    print(add(num_1, num_2))
elif operation == "-":
    print(subtract(num_1, num_2))
elif operation == "*":
    print(multiply(num_1, num_2))
elif operation == "/":
    print(divide(num_1, num_2))            