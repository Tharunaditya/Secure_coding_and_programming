# Boolean Exercise_1
# Let's check all the default boolean values of the types we know

# make
# an int
# a float
# a string
# the int 0
# the int 1
# the int 1000
an_int = 123
a_float = 3.14
a_string = "Hello, world!"
int_0 = 0
int_1 = 1
int_1000 = 1000
empty_str=''
# now print out all the `bool()` values using the bool() function
# are you surprised at the default boolean value for any python type?
print(bool(an_int))
print(bool(a_float))
print(bool(a_string))
print(bool(int_0))
print(bool(int_1))
print(bool(int_1000))
print(bool(empty_str))

'''All non-zero numbers (integers, floats) evaluate to True.
Empty strings and the integer 0 evaluate to False.
This behavior is consistent with how Python evaluates truthiness in conditional statements and logical operations.'''

