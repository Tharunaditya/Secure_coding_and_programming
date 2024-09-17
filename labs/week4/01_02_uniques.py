# Write code that creates a list of all unique values in a list.
# For example:
#
# list_ = [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]
# unique_list = [1, 2, 6, 55, 'hi', 4, 13,]

list_ = [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]

unique_list = []
for item in list_:
    if item not in unique_list:
        unique_list.append(item)

print(unique_list)
