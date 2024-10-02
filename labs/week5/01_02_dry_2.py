# rewrite your function from the previous exercise (01_01_dry.py)
# this time your function should be able change the divisible by number.

# I should be able to return the list of numbers which is divisible by "n", where
# 'n' can be any number.

## Input: a list of integers, a number 'n'
## output: a new list that only has retains numbers which are divisible by n

def check(List,n):
    div_2 = []
    for i in List:
     if i % n == 0:
        div_2.append(i)
    print(div_2)
  


samplelist=[10,20,12,21,35,45,63,65] 
check(samplelist,5)