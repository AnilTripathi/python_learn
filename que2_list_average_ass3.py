# Given a list of integers, compute the average of all numbers in the list.
def compute_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

# Example usage:
number_list = [1, 2, 3, 4, 5]
average = compute_average(number_list)
print(f"The average of the list is: {average}")