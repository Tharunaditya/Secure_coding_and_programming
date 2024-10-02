# Write a script that creates a dictionary of keys, `n`
# and values `n * n` for numbers 1 to 10. For example:
# result = {1: 1, 2: 4, 3: 9, ... and so on}

# use a for-loop

# Initialize an empty dictionary to store the result
result = {}

# Use a for-loop to iterate through numbers 1 to 10
for n in range(1, 11):
    # For each number, store the key as n and value as n * n
    result[n] = n * n

# Print the resulting dictionary
print(result)
