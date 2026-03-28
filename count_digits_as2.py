# Write a function to return the number of digits in a number.

def count_digits(n):
    if n <= 0:  # Check if the number is negative or zero
        print("Please enter a positive integer.")
        return 0
    
    count = 0
    
    while n > 0:
        n = n // 10
        count += 1
    
    return count

# Get user input for a number
number_input = int(input("Enter a positive integer: "))
digits_count = count_digits(number_input)
print(f"The number of digits in {number_input} is: {digits_count}")