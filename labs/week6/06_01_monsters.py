"""
Write 3 classes which are related to each other
1) a monster class
2) a night-monster class (they only come out at night)
3) a full moon monster class (they only come out at night and on the full moon)

Make use of inheritance to save your code!

## Monster class
# class attribute
time_of_day (will need to activate night monsters)
day_of_month
full_moon (boolean)

# attributes
name
number of limbs
attack mode (magic, physical, mental hypnosis etc)
scare factor
weakness
life points

# methods
basic attack (attack something)
sleep (get life points back)
defend (something attacks it!)

## Night monster
same as above, but also special powers that activate at night
vulnerable in daylight


## full moon monster
only active in the full moon
"""
import random

class Monster:
    # Class attributes
    time_of_day = "day"  # Can be "day" or "night"
    day_of_month = 1
    full_moon = False

    def __init__(self, name, limbs, attack_mode, scare_factor, weakness, life_points):
        self.name = name
        self.limbs = limbs
        self.attack_mode = attack_mode
        self.scare_factor = scare_factor
        self.weakness = weakness
        self.life_points = life_points

    def basic_attack(self):
        print(f"{self.name} attacks using {self.attack_mode} with a scare factor of {self.scare_factor}!")

    def sleep(self):
        recovered_points = random.randint(10, 20)
        self.life_points += recovered_points
        print(f"{self.name} sleeps and recovers {recovered_points} life points. Total life points: {self.life_points}")

    def defend(self, attack_type):
        if attack_type == self.weakness:
            damage = random.randint(20, 30)
            print(f"{self.name} is weak to {attack_type} and takes {damage} damage!")
        else:
            damage = random.randint(5, 15)
            print(f"{self.name} defends against the attack, taking only {damage} damage.")
        self.life_points -= damage
        print(f"{self.name}'s life points are now {self.life_points}.")

    def is_active(self):
        return True  # Basic monsters can be active at any time


class NightMonster(Monster):
    def __init__(self, name, limbs, attack_mode, scare_factor, weakness, life_points, special_power):
        super().__init__(name, limbs, attack_mode, scare_factor, weakness, life_points)
        self.special_power = special_power

    def basic_attack(self):
        if self.is_active():
            # Night monsters get an extra scare boost at night
            scare_boost = 5 if Monster.time_of_day == "night" else 0
            print(f"{self.name} attacks with {self.attack_mode} at scare factor {self.scare_factor + scare_boost}!")
        else:
            print(f"{self.name} is vulnerable in daylight and cannot attack!")

    def is_active(self):
        return Monster.time_of_day == "night"

    def use_special_power(self):
        if self.is_active():
            print(f"{self.name} uses their special power: {self.special_power}!")
        else:
            print(f"{self.name} cannot use their special power during the day.")


class FullMoonMonster(NightMonster):
    def is_active(self):
        # Full moon monsters are only active on a full moon night
        return Monster.time_of_day == "night" and Monster.full_moon

    def basic_attack(self):
        if self.is_active():
            print(f"{self.name} launches a terrifying full-moon attack with {self.attack_mode}!")
        else:
            print(f"{self.name} can only attack during a full moon night and remains hidden.")



Monster.time_of_day = "night"
Monster.full_moon = True
Monster.day_of_month = 15

# Creating instances of each monster type
generic_monster = Monster("Ghoul", limbs=4, attack_mode="physical", scare_factor=8, weakness="fire", life_points=100)
night_monster = NightMonster("Shade", limbs=2, attack_mode="mental hypnosis", scare_factor=12, weakness="light", life_points=120, special_power="Shadow Blend")
full_moon_monster = FullMoonMonster("Lycan", limbs=4, attack_mode="magic", scare_factor=15, weakness="silver", life_points=150, special_power="Lunar Rage")

# Running methods to demonstrate functionality
print("Generic Monster ")
generic_monster.basic_attack()
generic_monster.sleep()
generic_monster.defend("fire")

print("\n Night Monster ")
night_monster.basic_attack()
night_monster.use_special_power()
night_monster.defend("light")

print("\nFull Moon Monster")
full_moon_monster.basic_attack()
full_moon_monster.use_special_power()
full_moon_monster.defend("silver")
