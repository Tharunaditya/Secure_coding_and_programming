# wrtie a recursive fibonacci function


def fib(n):
    """
    input: 
        n: int

    return:
        fibbonacci number for n
    """
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)

print(fib(6)) #should return 8
print(fib(10)) #should return 55
