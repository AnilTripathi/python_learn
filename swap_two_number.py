# Write a program to swap the values of two numbers entered by the user.
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print("Before swapping:")
print("First number:", num1)
print("Second number:", num2)

# Swapping the values
num1, num2 = num2, num1

print("After swapping:")
print("First number:", num1)
print("Second number:", num2)