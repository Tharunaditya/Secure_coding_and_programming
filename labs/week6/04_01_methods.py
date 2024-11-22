"""
Create a class (you pick the name) that has
at least 5 methods.
3 of the methods must call other methods within them (using self.method name)
Run at least one method automatically in __init__ so it will run at start up

Demonstrate your methods work by creating an instance and running all the methods
"""
class Fruit:
    def __init__(self, name, color, taste, size):
        self.name = name
        self.color = color
        self.taste = taste
        self.size = size
        self.describe_fruit() 

    def describe_fruit(self):
        print(f"{self.name} is {self.size} in size and {self.color} in color.")
        self.guess_taste() 
    def guess_taste(self):
        if self.color == "Red":
            print("It might be sweet")
        elif self.color == "Green":
            print("It might be bitter or sour")
        else:
            print("Taste unknown")

    def eat(self):
        print(f"Eating {self.name}. It tastes {self.taste}!")

apple = Fruit("Apple", "Red", "sweet and delicious", "Medium")
banana = Fruit("Banana", "Yellow", "sweet", "Large")

apple.describe_fruit()
apple.eat()