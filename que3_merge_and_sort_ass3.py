# Input two lists of integers from the user. Merge them into one list and sort the result.
list1 = list(map(int, input("Enter the first list of integers separated by spaces: ").split()))
list2 = list(map(int, input("Enter the second list of integers separated by spaces: ").split()))

merged_list = list1 + list2
merged_list.sort()

print("The merged and sorted list is:", merged_list)