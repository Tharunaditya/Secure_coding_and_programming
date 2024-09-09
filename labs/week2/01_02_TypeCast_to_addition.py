# Type casting Exercise - 2
# Addition of string and integer using explicit conversion

# Initialise a string variable and integer variable
a = 10
b = "10"

# After explicit conversion, use python to successfully perform
b_int= int(b)
print(type(b_int))
# the addition of these variables - print the result to the console
result= a + b_int
print(result)
## Now try to convert this variable
c = "ten"
#int(c)
## What kind of error does python give?
#ValueError: invalid literal for int() with base 10: 'ten'
## What do you think the reason is?
# When you provide it with a string like "ten", which is a textual representation of a number, 
# it doesn't recognize it as a valid integer format. The int() function is 
# designed to handle strings that contain numerical digits, such as "10", "25", or "-3".