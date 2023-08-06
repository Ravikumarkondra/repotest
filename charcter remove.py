# write a python to remove character from string?

def character(input_string, remove_character):
    new_string = ''.join([char for char in input_string if char != remove_character])
    return new_string

input_string = input("Enter a string: ")
remove_character = input("Enter the character to remove: ")

result = character(input_string, remove_character)
print("Result:", result)
