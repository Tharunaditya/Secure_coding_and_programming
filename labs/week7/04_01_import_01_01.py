"""
Import your function from 01_01_sum_ints_inf_args.py
and use it here

Go back into your code and stop your print statements from showing up here

"""
from mymodule import *

tuple1 = (1, 2, 3, 4, 'hi', 'hi', (1, 2, 3), 10, ['a','b','c'])
their_sum = sum_integers(tuple1)
print(their_sum)
tuple2 = (2, 2, 2, 200.2,['a','b','c'],['a','b','c','d'], ['a','b','c','d','e'])
print(sum_integers(tuple2))

