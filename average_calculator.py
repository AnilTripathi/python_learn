# Ask the user to enter two integers and one float. Convert them all to floats and print their average.
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
num3 = float(input("Enter the float: "))
fnum1 = float(num1)
fnum2 = float(num2)

average = (fnum1 + fnum2 + num3) / 3
print("The average of", fnum1, ",", fnum2, "and", num3, "is", average)