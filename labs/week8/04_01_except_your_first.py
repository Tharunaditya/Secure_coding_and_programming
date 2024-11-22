"""
Write a function that accepts user input with the input() function
Try to convert their input to `int` and catch any exceptions that happen.

what kind of exceptions did you find?

"""

def convert(input):
  try:
    return int(input)
  except Exception as e:
    print(f"Exception error: {e}")
    return None
#   except ValueError as e:
#     print(f"Value error bro: {e}")
#     return None

input1 = "hello"

print("our input is ",input1,"which is", type(input1),
      "Our code converts it into", type(convert(input1)),
      "now our input is in ", type(input1),)
