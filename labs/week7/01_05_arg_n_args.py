# write a function that takes two positional arguments and uses *args
# your function should:
"""
arguments:
    name: name of person
    job: job title of person
    *args: possesions that they own

returns --> Str
   It should return a string that says a nice message like
  "hello Gilad, I heard your job of washing dishes allows you to own a lawn-mower, house, cat, and bat"

Remember, your string needs to _grow_ with the *args - it needs infinite potential!

"""

# name ="Gilad"
# job= "washing dishes"
# posses =('lawn-mower', 'house', 'cat', 'bat')
# posses_str = ", ".join(posses[:-1])
# if len(posses) > 1:
#   posses_str += f", and {posses[-1]}"
# elif posses:
#   posses_str = posses[0]
# print(f"Hello {name}, I heard your job of {job} allows you to own a {posses_str}.")
   

def describer(name,job,*posses):
  posses_str = ", ".join(posses[:-1])
  if len(posses) > 1:
    posses_str += f", and {posses[-1]}"
  elif posses:
    posses_str = posses[0]
  return f"Hello {name}, I heard your job of {job} allows you to own a {posses_str}."

message = describer('Tharunaditya','software','coding','debuging','fixing','testing','packaging')
print(message)