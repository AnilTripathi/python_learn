# Given a list, print all elements that appear more than once in the list
list1 = [1, 2, 3, 4, 5, 2, 6, 7, 8, 9, 1]
duplicates = []
for item in list1:
    if list1.count(item) > 1 and item not in duplicates:
        duplicates.append(item)
print("Elements that appear more than once:", duplicates)