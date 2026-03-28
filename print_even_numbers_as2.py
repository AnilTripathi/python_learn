# Write a function that takes two integers and prints all even numbers between them (inclusive)
def print_even_numbers(start, end):
    for num in range(start, end + 1):
        if num % 2 == 0:
            print(num)


print_even_numbers(1, 10)
print("---")
print_even_numbers(20, 30)