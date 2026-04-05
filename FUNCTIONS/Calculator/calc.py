def add(a, b):
    return a + b

def subtract(a , b):
        if a > b:
            return a - b
        else:
            return "Error: The first number must be greater than the second number for subtraction."

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero is not allowed."


num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print("Sum", add(num1, num2))
print("Difference:", subtract (num1, num2))
print("Product", multiply (num1, num2))
print("Quotient", divide(num1, num2))