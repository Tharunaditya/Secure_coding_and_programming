# Exercise

# stage 1

# Write a program to count the number of strings where the string length is 2 or more
# sample list: ['aaaa', 'a', 'ab', 'abc', ]
# result : 3

# count1 = 0
# for string in sample_list:
#     if len(string) >= 2:
#         count1 += 1


# print("Number of strings with length 2 or more:", count1)

## Stage 2
# Now count the number of strings that have length 2 or more
# AND the first and last character are same from a given list of strings.
sample_list = ['aaaa', 'a', 'ab', 'abc','rttr']
count2 = 0
for string in sample_list:
    if len(string) >= 2 and string[0]==string[-1]:
        count2 += 1
print("Number of strings with length 2 or more and same first and last characters:", count2)

# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2

