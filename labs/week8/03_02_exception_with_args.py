"""
rewrite inner_multiple from  Week 8

# write a function accepts as input an infinite amount of tuples
# it returns a list, where each element is the inner multiplication

# example input: (1,2), (2,2), (3,2), (4,5)
# output: [2,4,6,20]


Iterate over the args summing them up. 
Use an if statement ot check if the user passed tuples.
Raise an exception if they passed something else
"""

def inner_multiple(*args):
    result = []
    for item in args:
        if not isinstance(item, tuple):  # Checking if each argument is a tuple
            raise ValueError("All inputs must be tuples")
        inner_product = 1
        for num in item:
            inner_product *= num  # Multiplying each element within the tuple
        result.append(inner_product)
    return result


try:
    output = inner_multiple((1, 2), (2, 2), (3, 2), (4, 5))
    print(output)  # Expected output: [2, 4, 6, 20]
except ValueError as e:
    print(e)

# The function inner_multiple accepts a variable number of arguments (*args).
# It iterates over each argument (item), checking if it’s a tuple with isinstance(item, tuple).
# If any argument is not a tuple, it raises a ValueError.
# For valid tuples, it multiplies all elements inside the tuple to calculate the inner product and appends this product to the result list.
# The final list of inner products is returned.