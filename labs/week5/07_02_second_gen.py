def list_of_even_nums(start, stop):
    """
    Generates even numbers within a specified range.

    Args:
        start: The starting value (inclusive).
        stop: The ending value (exclusive).

    Returns:
        A generator object yielding even numbers.
    """
    for num in range(start, stop):
        if num % 2 == 0:
            yield num

# Create a generator using the function
my_gen = list_of_even_nums(2, 11)

# Iterate over the generator and print even numbers
for i in my_gen:
    print(i)

print("Second run!")
print()

# Iterate over the generator again (it will be empty)
for i in my_gen:
    print(i)