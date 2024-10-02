# Exercise

# Write a program to find the largest number in a list without using built-in functions

# [1,2,1,3,123123,2,1,3,6,3,1,23,6,123,1235,]
# output = 123123

# use a for loop
# Sample input
numbers = [1, 2, 1, 3, 123123, 2, 1, 3, 6, 3, 1, 23, 6, 123, 1235]

# Initializing the first number as the largest
largest = numbers[0]

# Loop through the list to find the largest number
for num in numbers:
    if num > largest:
        largest = num

# Output the largest number
print("The largest number is:", largest)
