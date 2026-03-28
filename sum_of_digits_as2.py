# Write a function to return the sum of digits in a number.
def sum_of_digits(n):
    if n <= 0:  # Check if the number is negative or zero
        print("Please enter a positive integer.")
        return 0

    total = 0
    while n > 0:
        total += n % 10
        n = n // 10

    return total

# Get user input for a number
number_input = int(input("Enter a positive integer: "))
digits_sum = sum_of_digits(number_input)
print(f"The sum of digits in {number_input} is: {digits_sum}")