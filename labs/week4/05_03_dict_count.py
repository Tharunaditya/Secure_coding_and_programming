# Exercise

# Write a program to create a dictionary from a string.
# Track the count of the letters from the string.
# Sample string : 'securecoding'
# Expected output: {'s': 1, 'e': 2, 'c': 2, 'u': 1, 'r': 1, 'o': 1, 'd': 1, 'i': 1, 'n': 1, 'g': 1}
# Sample string
sample_string = "securecoding"

# Initialize an empty dictionary to store the counts
letter_count = {}

# Iterate through each letter in the string
for letter in sample_string:
    # If the letter is already in the dictionary, increment its count
    if letter in letter_count:
        letter_count[letter] += 1
    else:
        # Otherwise, add the letter to the dictionary with a count of 1
        letter_count[letter] = 1

# Print the resulting dictionary
print(letter_count)
