# Write a program to check whether two lists share no common elements
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

if not set(list1) & set(list2):
    print("The lists share no common elements.")
else:
    print("The lists share common elements.")