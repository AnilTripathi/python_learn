# Letʼs create a “Number Guessing Game”. Given a secret number (already decided by you), 
# write a program that asks the user to guess it and prints: 
# • if the guess is above the number "Too high" 
# • if the guess is below "Too low" 
# • if the guess matches

secret_number = int(input("Enter the secret number: "))  # You can change this to any number you like
while True:
    guess = int(input("Guess the secret number: "))
    
    if guess < secret_number:
        print("Too low")
    elif guess > secret_number:
        print("Too high")
    else:
        print("Congratulations! You've guessed the number!")
        break