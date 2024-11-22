"""
implement a key-lookup procedure for a dictionary

Try to get the key and update the value by n
If an en exception is raised, handle it by creating the key with a default value
if no exception is raised, update the value
Regardless of what happens, print the dictionary
"""


def keylook(dic, key, inputvalue):
    try:
        dic[key] += inputvalue
    except KeyError:
        dic[key] = inputvalue
    finally:
        return dic


my_dict = {'a': 10, 'b': 20}
keylook(my_dict, 'a', 5)
print(my_dict)
keylook(my_dict, 'c', 3)
print(my_dict)
keylook(my_dict,'d',33)
print(my_dict)