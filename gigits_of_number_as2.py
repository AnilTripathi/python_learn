# Write a function that prints the digits of a number. For example, for the number 312, there are 3 digits: 3, 1, and 2 & we need to print them
def print_digits_str(number):
    for digit in str(number):
        print(digit)

def print_digits(n):
    if n<=0:  # Check if the number is negative or zero
        print("Please enter a positive integer.")
        return
    
    digits = []
    
    while n > 0:
        digit = n % 10
        digits.append(digit)
        n = n // 10

    # Print in correct order
    for d in reversed(digits):
        print(d)

print_digits_str(312)
print("---")
print_digits(312)