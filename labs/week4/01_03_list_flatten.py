#Exercise

# Write a Python program to flatten a shallow list

#Sample Input: [[2,4,3],[1,5,6], [9], [7,9,0]]
#Output: [2, 4, 3, 1, 5, 6, 9, 7, 9, 0]
# Sample input
shallow_list = [[2, 4, 3], [1, 5, 6], [9], [7, 9, 0]]

# Flattening the shallow list
flattened_list = []
for sublist in shallow_list:
    for item in sublist:
        flattened_list.append(item)

# Output the result
print(flattened_list)
