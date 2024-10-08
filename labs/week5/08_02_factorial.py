# write a recursive function to calculate the factorial


def factorial(n):
    
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
    """
    input: 
        n: int
    returns: 
        factorial of n
    
    reminder: factorial 8! is
    8*7*6*5*4*3*2*1
    """
    
print(factorial(8))