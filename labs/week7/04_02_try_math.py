""""
import the math library and use it to automatically generate a random list of numbers
You should generate 1000 random numbers.


"""
import math, random 


def generator(num_numbers):
  random_list = []
  for _ in range(num_numbers):
    random_number = random.randint(0,10000)  
    random_list.append(random_number)
  return random_list

print(generator(1000))