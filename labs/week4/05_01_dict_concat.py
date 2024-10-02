# Exercise

# Write a program to concatenate following dictionaries to create a new one.

# Sample Dictionary :
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50, 6:60}
# Expected Results: {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

# Sample dictionaries
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

# Concatenate dictionaries into a new one
result = {}

# Using the update() method to merge dictionaries
result.update(dic1)
result.update(dic2)
result.update(dic3)

# Print the result
print(result)
