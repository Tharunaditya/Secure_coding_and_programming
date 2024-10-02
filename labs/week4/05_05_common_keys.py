# Write a script that takes the following two dictionaries
# and creates a new dictionary by combining the common keys
# and adding the values of duplicate keys together.
# Use `for` loops to iterate over these dictionaries
# to accomplish this task.
#
# Example output:
# result = {"a": 3, "b": 2, "c": 7 , "d": 2}

dict_1 = {"a": 1, "b": 2, "c": 3}
dict_2 = {"a": 2, "c": 4, "d": 2}

# Initialize an empty dictionary to store the result
result = {}

# Iterate through the first dictionary
for key in dict_1:
    if key in dict_2:
        # If the key is in both dictionaries, sum the values
        result[key] = dict_1[key] + dict_2[key]
    else:
        # If the key is only in dict_1, add it as is
        result[key] = dict_1[key]

# Iterate through the second dictionary to add keys not present in dict_1
for key in dict_2:
    if key not in result:
        result[key] = dict_2[key]

# Print the resulting dictionary
print(result)
