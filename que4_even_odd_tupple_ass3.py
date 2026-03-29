# Given a tuple of integers, create: 
# • A tuple of all even numbers 
# • A tuple of all odd numbers


numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
even_numbers = tuple(x for x in numbers if x % 2 == 0)
odd_numbers = tuple(x for x in numbers if x % 2 != 0)
print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)