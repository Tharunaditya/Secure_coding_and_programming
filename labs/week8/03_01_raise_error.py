"""
Write a function that accepts user input with the input() function
Specify that they must use alphabet characters only.
Then raise an exception if they enter anything that is not able an alphabet character!

Hint: you can use .isalpha() to check if a character is an alpha character.
"""

def get_alpha_input():
    user_input = input("Enter alphabet characters only: ")
    if not user_input.isalpha():
        raise ValueError("Invalid input! Please enter alphabet characters only.")
    return user_input

# Example usage
try:
    result = get_alpha_input()
    print(f"You entered: {result}")
except ValueError as e:
    print(e)


# To understand
# The function get_alpha_input() prompts the user to input alphabet characters.
# It checks if the input contains only alphabetic characters using isalpha().
# If the input contains non-alphabet characters, it raises a ValueError with an error message.
# In the try-except block, we handle the exception and print the error message if it occurs.
# This will ensure that only alphabet characters are accepted.
