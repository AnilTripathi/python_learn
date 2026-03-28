# Design a program to continuously input a number from user & print if it is positive or negative until the user enters “Quit”

while True:
    user_input = input("Enter a number (or type 'Quit' to exit): ")
    
    if user_input.lower() == "quit":
        print("Exiting the program. Goodbye!")
        break
    
    number = float(user_input)
    if number > 0:
        print(f"{number} is a positive number.")
    elif number < 0:
        print(f"{number} is a negative number.")
    else:
        print("The number is zero.")