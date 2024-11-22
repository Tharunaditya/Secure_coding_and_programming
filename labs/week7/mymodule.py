# write a function that takes an infinite number of arguments
# it should check if the argument are integers and then sum all integeres
# it should return the sum of all the arguments


# example
# input: 1,2,3,4,'hi','hi',(1,2,3), 10
# output: 20

# example 2
# input: 2,2,2,200.2           # **note*** that 200.2 is _not_ an integer, so we don't sum it.
# output: 6

def sum_integers(*args):
    total = 0
    for arg in args:
        if isinstance(arg, int):
            total += arg
        elif isinstance(arg, (list, tuple)):
            for item in arg:
                total += sum_integers(item)  
    return total
good = "The good cause"
bad = "Hi"
# print(sum_integers(1, 2, 3, 4, 'hi', 'hi', (1, 2, 3), 10, ['a','b','c'])) 
# print(sum_integers(2, 2, 2, 200.2,['a','b','c'],['a','b','c','d'], ['a','b','c','d','e'])) 