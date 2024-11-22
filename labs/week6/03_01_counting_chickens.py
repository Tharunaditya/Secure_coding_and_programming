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
# first intializing the class Chicken and its attributes time_of_day as night and the number of eggs laid as 0 

class Chicken:
    time_of_day = 0
    number_of_eggs_laid = 0
# intializing the slef with the bred gender weight and lays_eggs arguments 
    def __init__(self, breed, gender, weight, lays_eggs):
        self.breed = breed
        self.gender = gender
        self.weight = weight
        self.lays_eggs = lays_eggs
        self.eggs_laid = 0    #  starting the   eggs_laid as  0

    def lay_egg(self):
        #checking the time of the day and the eggs can be layed or not then
        if self.lays_eggs and (self.time_of_day >= 18 or self.time_of_day <= 6):
            if random.choice([True, False]): # randomly determining whether the egg is laid or not by using random choice among the True or False boolean
                self.eggs_laid += 1  # if true eggs laid increased  , 
                Chicken.number_of_eggs_laid += 1 # incremnent in the number of eggs laid in the chicken class

chickens = [] # intializing the chicken list to store the 100 instances of the chicken class and appending them into the chicken list 
# given that in question 100 instances so we are taking the 100 in range
for i in range(100):
    chickens.append(Chicken(breed='Breed', gender='Female', weight='2kg', lays_eggs=True))
# simulating the laying eggs for every year
for hour in range(24): # for every hour in 24 hours
    Chicken.time_of_day = hour # that the time of the day is that particular hour 1 , 2, 3, 4  . . .   so on
    for chicken in chickens: # for each chicken in the chickens list 
        chicken.lay_egg()  # chicken will lay egg 

total_eggs = Chicken.number_of_eggs_laid   # total eggs stored here by calling the class with its attribute
average_eggs_per_chicken = total_eggs / 100 # calculating the average eggs per chicken by dividing the total eggs by 100 (total instances)

for idx, chicken in enumerate(chickens):   # idx is like the number of chicken from 1 to 100
    print(f"Chicken {idx + 1} laid {chicken.eggs_laid} eggs.") # as the id starts with 0 index 0 we add 1 on each idx and call the  each chciken number of eggs laid
print("Average eggs per chicken:", average_eggs_per_chicken) # Average printing