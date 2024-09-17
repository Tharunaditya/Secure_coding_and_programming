# You start this journey with a number `n`.
# You have to display a string representation of all numbers from 1 to n,
# but there are some constraints:
# - If the number is divisible by 3, write `Fizz` instead of the number
# - If the number is divisible by 5, write `Buzz` instead of the number
# - If the number is divisible by both 3 and 5, write `FizzBuzz` instead of the number

# feel free to adjust n for debugging

n = 15
result = []
for i in range(1, n+1):
    if i % 3 == 0 and i % 5 == 0:
         result.append("FizzBuzz")
    elif i % 3 == 0:
         result.append("Fizz")
    elif i % 5 == 0:
         result.append("Buzz")
    else:
            result.append(str(i))


# Example usage:
for i in result:
    print(i)
