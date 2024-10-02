# With the given sets `s` and `t`, demonstrate how you can:
# - Create an intersection of both sets
# - Create a union of both sets

s = {1, 2, 3, 4}
t = {3, 4, 5, 6}

intersection_set = s.intersection(t)
print("Intersection:", intersection_set)  # Output: {3, 4}

union_set = s.union(t)
print("Union:", union_set)  # Output: {1, 2, 3, 4, 5, 6}