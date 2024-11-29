"""
Use JSON to serialize the following dictionary

"""

# my_dict = {i: i ** 2 for i in range(10_000)}

# after creating your JSON file, try opening it the file by double clicking it in the explorer
# can you read it ? Why or why not?

# use code to load your json file into a new variable
# print it out to make sure it's the same.

import json


my_dict = {i: i ** 2 for i in range(10_000)}
# I am  Serializing  the dictionary to a JSON file
with open('my_dict.json', 'w') as json_file:
    json.dump(my_dict, json_file)

print("Dictionary has been serialized and saved to 'my_dict.json'.")

# Try opening the file manually to see if it’s readable.
# Now load the JSON back into a new variable
with open('my_dict.json', 'r') as json_file:
    loaded_dict = json.load(json_file)

# Verify the loaded dictionary is the same as the original
print("Dictionary successfully loaded. Is it the same? ", loaded_dict == my_dict)