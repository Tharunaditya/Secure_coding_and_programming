# Which of the following strings is the longest?
# Use the len() function to find out.
# You can run `len(my_variable)` and it will return the len of the variable (in this case it's a string)

longest_german_word = "Donaudampfschifffahrtsgesellschaftskapitänskajütentürschnalle"
longest_hungarian_word = "Megszentségteleníthetetlenségeskedéseitekért"
longest_finnish_word = "Lentokonesuihkuturbiinimoottoriapumekaanikkoaliupseerioppilas"
strong_password = "%8Ddb^ca<*'{9pur/Y(8n}^QPm3G?JJY}\\(<bCGHv^FfM}.;)khpkSYTfMA@>N"

lenofgerman=len(longest_german_word)
lenofhungarian=len(longest_hungarian_word)
lenoffinnish=len(longest_finnish_word)
lenofstron=len(strong_password)

# Now that you know what the longest word is, print it out in an f-string below
print(lenofgerman,lenofhungarian,lenoffinnish,lenofstron)
print(f"the longest word of above words is {strong_password}")