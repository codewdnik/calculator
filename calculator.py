def add(x, y):
    return x + y

def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

# Main program loop
while True:
    num1 = float(input("Enter the first number: "))
    operator = input("Enter the operator: ")
    num2 = float(input("Enter the second number: "))

    if operator == "+":
        result = add(num1, num2)
    elif operator == "-":
        result = subtract(num1, num2)
    elif operator == "*":
        result = multiply(num1, num2)
    elif operator == "/":
        result = divide(num1, num2)
    else:
        print("Invalid operator")
        continue

    print("Result:", result)
