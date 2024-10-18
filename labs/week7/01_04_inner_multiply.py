# write a function accepts as input an infinite amount of tuples
# it returns a list, where each element is the inner multiplication

# example input: (1,2), (2,2), (3,2), (4,5)
# output: [2,4,6,20]

def tupmul(*tuples):
    result = []
    for tup in tuples:
        product = 1
        for item in tup:
            product *=item
        result.append(product)
    return result

print(tupmul((1,2), (2,2), (3,2), (4,5)))
        
