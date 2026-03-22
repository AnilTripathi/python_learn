# Take a decimal number as input (like 1045.78) and output its: 
# • integer part (45) 
# • fractional part (-.78)

# Take decimal number input from user
num = float(input("Enter a decimal number: "))
str_num=str(num)

# Split the number into integer and fractional parts
integer_part_str, fractional_part_str = str_num.split('.')

# Get integer part
integer_part = int(integer_part_str)

# Get fractional part
fractional_part = float('0.' + fractional_part_str)

# Print results
print("Integer part:", integer_part)
print("Fractional part:", fractional_part)