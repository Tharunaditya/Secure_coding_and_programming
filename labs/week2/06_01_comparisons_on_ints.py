# Run some basic comparisons on basic integers and floating points

# what is bigger, a or b?
a = 2
b = 10
print(a>b)
print(b>a)
result1 = "a is greater" if a>b else "b is greater"
print(result1)
# What is smaller , c or d?
c = 2.02
d = 2.01119999
print(c>d)
print(c<d)
result2 = "c is greater" if c>d else "d is greater"
print(result2)
# what is bigger e or f?
e = float("inf")
f = 12912912912091928312903713582043754302895723048957
result3 = "e is greater" if e>f else "f is greater"
print(result3)
# are these equal?

g = 1.02020202020
i = 1.0202020202011111
result4 = "g and i equal" if g==i else "g and i are not equal"
print(result4)