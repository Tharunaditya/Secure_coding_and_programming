# use a for loop with enumerate to go over the long word and
# sum all the indices for every single vowel

# example:
#
# input: "hi I me
# i=1, I=3, e = 6,
# the sum is: 10

a_long_word = "the quick brown fox jumped over the lazy dog and then ran around and got very happy happy happy yes!"
# the sum should be 1147 (you can check your code with this)

vowels = "aeiouAEIOU"
vow_sum = 0
for index, char  in enumerate(a_long_word):
    if char in vowels:
        vow_sum += index
print(vow_sum)