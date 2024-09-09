# 1) Initialize variable a to true, b to false and c to true
a = True
b = False
c = True

# 2) If you print(a and b or c) what it will return? Why?
# Does the order of operations matter?
print(a and b or c)
'''
Yes, the order of operations matters in this case. If the or operation were evaluated first, the result would be different.
'''
# 3) Is print(a or b and c) different?

print(a or b and c)
'''
Due to operator precedence, the and operation is performed first.
b and c evaluates to False because both b and c must be True for the and operation to be True.
a or False evaluates to True because a is True.
'''
# 4)Assign c to false and print the value of a and b or c

c= False
print(a and b or c)
# Understand the difference in each scenario
# What is happening here?
'''
a and b is still False because both a and b must be True for the and operation to be True.
False or False evaluates to False.
'''

# 5) Now try to use some ()'s to force python to evaluate it differently.
print((a and b) or c)  # Output: False
print(a or (b and c))  # Output: True