# Take two numbers as input from the user and print their sum, difference, product, and quotient

num1=float(input("Enter the first number: "))
num2=float(input("Enter the second number: "))

sum=num1 + num2
difference=num1 - num2
product=num1 * num2
if num2 != 0:
    quotient=num1 / num2
else:
    quotient="Undefined (division by zero)"
    
    
print("The sum of",num1,"and",num2,"is",sum)
print("The difference of",num1,"and",num2,"is",difference)
print("The product of",num1,"and",num2,"is",product)
print("The quotient of",num1,"and",num2,"is",quotient)