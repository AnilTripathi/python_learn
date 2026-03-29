# Ask the user for a string and check whether it is a palindrome or not. 
# A string which is same when we read it forward & backward. Eg-“madam”,“racecar” etc

def is_palindrome(s):
    # Remove spaces and convert to lowercase for uniformity
    cleaned_string = s.replace(" ", "").lower()
    
    # Check if the cleaned string is equal to its reverse
    return cleaned_string == cleaned_string[::-1]

# Get user input for a string
user_input = input("Enter a string: ")
if is_palindrome(user_input):
    print(f"'{user_input}' is a palindrome.")
else:
    print(f"'{user_input}' is not a palindrome.")