# Exercise

# Write a program to move all zero digits to end of a given list of numbers
# Expected output:
# Original list:

# [3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9, 7, 1]
# Move all zero digits to end of the said list of numbers:

# [3, 4, 6, 2, 6, 7, 6, 9, 10, 7, 4, 4, 5, 3, 2, 9, 7, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# Sample input
numbers = [3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9, 7, 1]

# List to store non-zero numbers
non_zero_list = []

# Count of zeros
zero_count = 0

# Loop through the list to separate zeros and non-zeros
for num in numbers:
    if num == 0:
        zero_count += 1
    else:
        non_zero_list.append(num)

# Add the zeros to the end
non_zero_list.extend([0] * zero_count)

# Output the result
print("Original list:")
print(numbers)
print("\nMove all zero digits to end of the said list of numbers:")
print(non_zero_list)
