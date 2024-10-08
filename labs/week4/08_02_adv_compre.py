# write code to generate a dictionary where
# each key is:an integer divisible by 3
# each value is: a list containing the even numbers in the range of key

# Take all the numbers divisible by 3 from 1-301
# example output
# {3: [2], 6: [2,4,6], 9:[2,4,6,8].... 300:[2,4,6,...288]}

dictionary = {}

for key in range(3, 302, 3):
    values = [num for num in range(2, key + 1, 2)]
    dictionary[key] = values

print(dictionary)