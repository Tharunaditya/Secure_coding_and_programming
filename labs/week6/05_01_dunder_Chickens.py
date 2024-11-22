"""
Update your chicken class to include the following dunders

__str__  : make some nice str format for your chicken. 
When we print your chicken it should tell us: how heavy the chicken is, the gender and how many eggs it has laid (if has)

__add__ : what happens when you add two chickens together? If they are male and female, create a baby chicken! (a new chicken) Otherwise, nothing?

"""
import random

class Chicken:
    time_of_day = 0
    number_of_eggs_laid = 0

    def __init__(self, breed, gender, weight, lays_eggs):
        self.breed = breed
        self.gender = gender
        self.weight = weight
        self.lays_eggs = lays_eggs
        self.eggs_laid = 0

    def lay_egg(self):
     
        if self.lays_eggs and (self.time_of_day >= 18 or self.time_of_day <= 6): # in 24 hours format
            if random.choice([True, False]):  # Randomly decide if the chicken lays an egg
                self.eggs_laid += 1 # when egg gets layed  increment the eggs laid
                Chicken.number_of_eggs_laid += 1 #increasing the class attribute too

    def __str__(self):
  
        eggs_info = f" and has laid {self.eggs_laid} eggs" if self.eggs_laid else ""
        return f"A {self.weight} {self.gender} {self.breed} chicken{eggs_info}."

    def __add__(self, other):
       
        if isinstance(other, Chicken) and ((self.gender == "Female" and other.gender == "Male") or
                                           (self.gender == "Male" and other.gender == "Female")):
            return Chicken(breed=self.breed, gender=random.choice(["Male", "Female"]), weight="0.5kg", lays_eggs=True)
        return None


chickens = [Chicken(breed='Breed', gender='Female', weight='2kg', lays_eggs=True) for _ in range(100)]


for hour in range(24):
    Chicken.time_of_day = hour
    for chicken in chickens:
        chicken.lay_egg()

total_eggs = Chicken.number_of_eggs_laid
average_eggs_per_chicken = total_eggs / len(chickens)

for idx, chicken in enumerate(chickens):
    print(f"Chicken {idx + 1}: {chicken}")
print("Average eggs per chicken:", average_eggs_per_chicken)


chicken1 = Chicken("Breed", "Female", "2kg", True)
chicken2 = Chicken("Breed", "Male", "2kg", False)
baby_chicken = chicken1 + chicken2

if baby_chicken:
    print("A new baby chicken is born!")
    print(baby_chicken)
else:
    print("No baby chicken was born.")
