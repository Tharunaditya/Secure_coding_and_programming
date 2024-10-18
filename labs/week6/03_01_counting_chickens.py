"""
create a chicken class that has the following

# class attributes
time_of_day
number_of_eggs_laid

# instance attributes (uses the self variable)
breed
gender
weight
lays_eggs (boolean)

# methods
lay_egg --> this function should depend on time of day (chickens only lay eggs at night!),
it should also use random numbers to deterimine if laying the egg worked or not


## Create 100 instances of your chickens using a for loop

Use a for loop to update the time of day (go through each hour of the day)
within the loop have your chickens all try to lay eggs
Afterwards, print out how many total eggs were hatched -- for all chickens and individually.
What was the average number of eggs per chicken?
"""
import random

class Chicken:
     # First we are intialising the class attributes 
    time_of_day = 0
    number_of_eggs_laid = 0
    # then we take the arguments for the class and specify them as self 
    def __init__(self, breed, gender, weight, lays_eggs):
        self.breed = breed
        self.gender = gender
        self.weight = weight
        self.lays_eggs = lays_eggs
        self.eggs_laid = 0

    def lay_egg(self):
        if Chicken.time_of_day == 0 and self.lays_eggs:  # Chickens lay eggs at night (time_of_day == 0)
            if random.choice([True, False]):  # Randomly decide if an egg is laid
                self.eggs_laid += 1
                Chicken.number_of_eggs_laid += 1

# Creating Instances and Simulate Egg Laying
chickens = [Chicken("Breed", "Female", "2kg", True) for _ in range(100)]

# Simulating each hour of the day (24 hours)
for hour in range(24):
    Chicken.time_of_day = hour
    for chicken in chickens:
        chicken.lay_egg()

# Print Results
total_eggs = Chicken.number_of_eggs_laid
average_eggs_per_chicken = total_eggs / 100

print(f"Total eggs laid by all chickens: {total_eggs}")
print(f"Average number of eggs per chicken: {average_eggs_per_chicken}")

for idx, chicken in enumerate(chickens):
    print(f"Chicken {idx + 1} laid {chicken.eggs_laid} eggs.")
