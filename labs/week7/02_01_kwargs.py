## write a function that uses **kwargs as input
## it should print out the sum of all the integers found in the values

"""
input: hi = 2020, bye = 1000, see = 2, def = 'this'
output : 3022

The function should work for any kind of values and as many keyword arguments as the use would like to pass

"""
'''
in a function definition allows you to pass a variable number 
of keyword arguments to the function. It's a dictionary-like structure and is
extremely handy for building flexible functions. Here's a basic example:
'''
def sumargs(**kwargs):
    total = 0
    for key, value in kwargs.items():
        if type(value) is int:
            total += value
    print(total)


sumargs(hi=2020, bye=1000, see=2, dear=990, )
