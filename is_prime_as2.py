# Write a function that returns True if a number is a prime number and False otherwise, using a loop.
# is_prime(n) -> True/False
# [-Hint1: We only check prime for 2 or numbers greater than 2. 2 is the smallest prime number.
# 22: A number, n, will always get divided by at least one number in range [2, n-1].
# non-Prime e.g.: For number weʼll check in range (2,8) & itʼll get divided by 3. So itʼs non-prime & weʼll return false for it.
# 99: For number weʼll check in range (2,6) & it wonʼt get divided by any. So itʼs prime & weʼll return true for it.]

def is_prime(n):
    if n <= 1:  # Check if the number is less than or equal to 1
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def is_prime_enhance(n):
    if n < 2:
        return False
    
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    
    return True

# Get user input for a number
number_input = int(input("Enter a positive integer: "))
if is_prime(number_input):
    print(f"{number_input} is a prime number.")
else:
    print(f"{number_input} is not a prime number.")
    
if is_prime_enhance(number_input):
    print(f"{number_input} is a prime number (enhanced check).")
else:
    print(f"{number_input} is not a prime number (enhanced check).")    
