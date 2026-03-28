# Letʼs create a Simple Calculator that performs arithmetic operations. Create a function that performs addition, subtraction, multiplication, or division based on the parameter.
# Calculator calculator(a, b, operation) operation [parameter can have values '+', '-', '*', '/']. operation ‘+’ ‘-’ '*’ ‘/’

def calculator(a, b, operation):
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '*':
        return a * b
    elif operation == '/':
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero is not allowed."
    else:
        return "Error: Invalid operation."
    
# Example usage:
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
op = input("Enter the operation (+, -, *, /): ")

result = calculator(num1, num2, op)
print(f"The result of the operation is: {result}")