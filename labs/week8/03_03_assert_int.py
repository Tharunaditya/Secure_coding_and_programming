"""
write a function that asks for user input with the input() function
Ask them to create a password that is greater than >6 and <12 characters long ( 6< pwd < 12)

Use an assert statement to validate their password choice

"""
# def create_password():
#     password = input("Create a password (must be between 7 and 11 characters long): ")
#     assert 6 < len(password) < 12, "Password must be greater than 6 and less than 12 characters."
#     return password

# try:
#     result = create_password()
#     print("Password created successfully!")
# except AssertionError as e:
#     print(e)


# Input Prompt: The function create_password() prompts the user to enter a password.
# Password Length Check: An assert statement checks that the password length is greater than 6 and less than 12 characters.
# len(password): Calculates the length of the entered password.
# 6 < len(password) < 12: Ensures the length is within the acceptable range.
# AssertionError Handling: If the password does not meet the length requirement, an AssertionError is raised, displaying the message "Password must be greater than 6 and less than 12 characters.".
# try-except Block: In the try-except block, the AssertionError is caught and printed if triggered, providing feedback to the user about the password requirement.

def create_password():
    password = input("Create a password (must be between 7 and 11 characters long): ")
    assert 6 < len(password) < 12, "password must be greater than 6 and less than 12 characters."
    print("password created successfully!")
    return password


create_password()
