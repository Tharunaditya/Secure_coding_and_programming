# write a script that will "sing" a song that goes like this
#  "there are 100 jars of payasam on the counter ...... now i ate one!"
# "there are 99 jars of payasam on the counter ... now I ate one!"
#
#
# "there are 0 jars of payasam on the counter - none left to eat!"
# "now I will go vomit...."

# you must use a while loop to do it

jars = 100

while jars > 0:
  print(f"There are {jars} jars of payasam on the counter...")
  jars -= 1
  print("Now I ate one!")

print("There are 0 jars of payasam on the counter - none left to eat!")
print("Now I will go vomit...")