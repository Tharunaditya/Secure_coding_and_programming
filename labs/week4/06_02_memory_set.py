# MEMORY GAME WITH SETS
# Continuously collect number input from a user with a `while` loop.
# Confirm that the input can be converted to an integer,
# then add it to a Python `set()`.
# If the element was already in the set, notify the user that their
# their input is a duplicate and deduct a point.
# If the user loses 5 points, quit the program.
# They win if they manage to create a set that has more than 10 items.

# you will need the `input()` function to collect information from the user

score = 0
unique_numbers = set()

while True:
  try:
    number = int(input("Enter a number: "))
    if number in unique_numbers:
      print("Duplicate! You lose a point.")
      score -= 1
    else:
      unique_numbers.add(number)
      print("Number added successfully.")
  except ValueError:
    print("Invalid input. Please enter a valid number.")

  if score == -5:
    print("Game over! You lost 5 points.")
    break
  elif len(unique_numbers) > 10:
    print("Congratulations! You won the game.")
    break