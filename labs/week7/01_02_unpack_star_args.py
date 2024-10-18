## unpack the following list into 3 variables

my_list = [1, 2, 3, 1, 23, 12, 31, 2, 2, 2, 2, 3, 2, 3, 2, 3, 2, 3, 21, 2, 3, 1]

# the first variable should contain the first element
# the second variable should contain the second element
# the last variable should contain _the rest of the elements_

## hint: use the * unpacking operator.

# first=my_list[0]
# print(first)
# second=my_list[1]
# print(second)
# rest = my_list[2:]
# print(rest)

first, second, *rest = my_list

print(first)
print(second)
print(rest)

