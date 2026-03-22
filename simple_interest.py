# Ask the user for: Principal (P), Rate (R), Time (T). Convert all to floats and compute simple interest: float SI = (P * R * T) / 100


principal = float(input("Enter the principal amount (P): "))
rate = float(input("Enter the rate of interest (R): "))
time = float(input("Enter the time in years (T): "))

simple_interest = (principal * rate * time) / 100

print("The simple interest is:", simple_interest)
