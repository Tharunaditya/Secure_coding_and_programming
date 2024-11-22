"""
Write a function that takes two inputs and attempts to add them together.

Use a try/except block to catch all possible errors

Try adding
int + int
int + str
str + list
tuple + list
dict + dict
dict + str

Are all the exceptions the same?
"""

def adder():
    a = input("Enter 1st element :")
    b = input ("Enter 2nd element :")
    try:
        return int(a)+int(b)
    except ValueError as e:
        print(f"A invalid error occured: {e}")
    except Exception as e:
        print(f"An invalid error occured : {e}")

print(adder())