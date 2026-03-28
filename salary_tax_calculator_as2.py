# Write a program that takes as input. Using conditional statements, calculate the final tax rate based on the following rules: 
# salary final tax rate 
# • If salary < 30,000 → 5% 
# • If salary is 30,000–70,000 → 15% 
# • If salary > 70,000 → 25%

def calculate_tax_rate(salary):
    if salary < 30000:
        tax_rate = 5
    elif 30000 <= salary <= 70000:
        tax_rate = 15
    else:
        tax_rate = 25
    return tax_rate

# Get user input for salary
salary_input = float(input("Enter your salary: "))
tax_rate = calculate_tax_rate(salary_input)
print(f"The final tax rate for a salary of {salary_input} is: {tax_rate}%")