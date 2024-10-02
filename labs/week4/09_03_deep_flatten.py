# # Make your list flatten code do a DEEP flatten and account for other datatypes

# hard_nested_list = [
#     [1, 2, [1, [1, 2], 2], 3, 4],
#     [5, 6],
#     [7, 8, 9],
#     "shiva",
#     10,
#     [1, 2, [8, 9,], "Devi"],
#     10.0,
#     (1, 2),
# ]

# # should get back
# # [1, 2, 1, 1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 'brandon', 10, 10.0, 1, 2]

# many_nests = ["a", ["bb", ["ccc", "ddd"], "ee", "ff"], "g", "h"]
# # should get back
# # ['a', 'bb', 'ccc', 'ddd', 'ee', 'ff', 'g', 'h']
# Flatten a nested list, including lists within tuples and strings
#   """Deeply flattens a nested list, handling lists within tuples and strings.

#     Args:
#         nested_list: The nested list to be flattened.

#     Returns:
#         A flattened list containing all elements from the original nested list.
#     """

# def deep_flatten(nested_list):
#     flattened_list = []
#     for item in nested_list:
#         if isinstance(item, list) or isinstance(item, tuple):
#             flattened_list.extend(deep_flatten(item))
#         elif isinstance(item, str):
#             flattened_list.extend(list(item))  # Convert string to list of characters
#         else:
#             flattened_list.append(item)
#     return flattened_list

def deepflat(nestedlist):
    deepflat_list =[]
    for item in nestedlist:
        if type(item) is list or type(item) is tuple:
            deepflat_list.extend(deepflat(item))
        elif type(item) is str:
            deepflat_list.extend(list(item))
        else:
            deepflat_list.append(item)
    return deepflat_list
        
hard_nested_list = [[1, 2, [1, [1, 2], 2], 3, 4], [5, 6], [7, 8, 9], "shiva", 10, [1, 2, [8, 9,], "Devi"], 10.0, (1, 2)]
many_nests = ["a", ["bb", ["ccc", "ddd"], "ee", "ff"], "g", "h"]

flattened_hard_list = deepflat(hard_nested_list)
flattened_many_nests = deepflat(many_nests)

print(flattened_hard_list)
print(flattened_many_nests)