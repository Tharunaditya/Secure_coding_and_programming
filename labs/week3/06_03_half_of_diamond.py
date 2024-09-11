#Exercise

#Write a Python program to construct the following pattern, using a nested for loop.
"""
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
*
"""
rows = 5  # Adjust the number of rows as needed
for i in range(rows):
    for j in range(i + 1):
        print("* ", end="")
    print()

for i in range(rows - 1, 0, -1):
    for j in range(i):
        print("* ", end="")
    print()