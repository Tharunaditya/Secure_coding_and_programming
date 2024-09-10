# write a short command line game
name = str(input("Please enter your name:"))
# 1. ask the user for their name: (use the input() function)
print(f"Hello {name}")

# Say hello to them with their name
# If their name begins with a vowel say something funny about that ("Aha! Oho! Uhu! Ihi! etc", your name begins with a vowel!)
# If their n ame begins with a consonant make an even better joke about it.
vowels = ['a','e','i','o','u']
if name[0].lower() in vowels:
    print(f" Aha! Oho! Uhu! Ihi! etc your {name} starts with vowel")
else:
    print(f"yellow yellow {name} is dirty fellow because your name starts with consonant")

# Ask them to pick a number between 1 and 10.
# If they guessed the right number, tell them they won
# Else, tell them they lost.
import random

random_number = random.randint(0, 10)

numb=int(input("Please enter a number between 1 and 10: "))

if random_number == numb:
    print("Hurray ! your number is correct")
else:
    print("You are wrong !!")

