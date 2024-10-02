### This code creates a random list for you to use
import random

list_length = random.randint(1, 20)
randlist = list()
for i in range(list_length):
    randlist.append(random.randint(1, 100))


# Write a script that takes randlist (a list of numbers) and:
#     - sorts the numbers
#     - stores the numbers in tuples of two in a new list
#     - prints each tuple
#
# If the list has an odd number of items,
# add the last item to a tuple together with the number `0`.

# Note: This lab might be challenging! Make sure to discuss ask questions
# and get help!  You will need a python function called `sort`

# example input :[1,2,5,1,2]
# example output :[(1,1), (2,2), (5,0)]

# Sort the list
randlist.sort()

# Create a new list to hold tuples
tuple_list = []

# Iterate over the list and group numbers into tuples of two
for i in range(0, len(randlist), 2):
    if i + 1 < len(randlist):
        # If there's a pair of numbers, add them as a tuple
        tuple_list.append((randlist[i], randlist[i + 1]))
    else:
        # If there's only one number left, pair it with 0
        tuple_list.append((randlist[i], 0))

# Print each tuple
for tup in tuple_list:
    print(tup)

# Example of the generated random list and the output tuples
print("Original List:", randlist)
print("Tuples List:", tuple_list)
