#write a python program to check string is palindrome or not?



def palindrome(input_string):
    cleaned_string = input_string.lower().replace(" ", "")
    return cleaned_string == cleaned_string[::-1]

input_string = input("Enter a string: ")

if palindrome(input_string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
