# Use string indexing and string concatenation (or f-strings)
# to write the sentence "we see trees" only by picking
# the necessary letters from the given string.

word = "tweezers "

sentence = f"{word[1]}{word[2]} {word[7]}{word[2]}{word[2]} {word[0]}{word[6]}{word[2]}{word[2]}{word[7]}"
print(sentence)