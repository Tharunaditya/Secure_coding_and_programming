# Use a `for` loop to iterate over the story text
# and string slicing to translate it to ~pig latin.
# For the purpose of this program, we will say that any word or name can be
# translated to pig latin by moving the first letter to the end, followed by "ay".
# You'll need to use conditional statements to decide when a word is over.
#
# For example: You would never guess --> ouyay ouldway evernay uessgay


story = """

At a great meeting of the Animals, who had gathered to elect a new ruler, the Monkey was asked to dance. This he did so well, with a thousand funny capers and grimaces, that the Animals were carried entirely off their feet with enthusiasm, and then and there, elected him their king.

The Fox did not vote for the Monkey and was much disgusted with the Animals for electing so unworthy a ruler.

One day he found a trap with a bit of meat in it. Hurrying to King Monkey, he told him he had found a rich treasure, which he had not touched because it belonged by right to his majesty the Monkey.

The greedy Monkey followed the Fox to the trap. As soon as he saw the meat he grasped eagerly for it, only to find himself held fast in the trap. The Fox stood off and laughed.

"You pretend to be our king," he said, "and cannot even take care of yourself!"

Shortly after that, another election among the Animals was held.
"""

words = story.split() # first words are getting slip and added into words bank
translated_words = [] # intiating an empty list translated_words = [] where we are going to add the words translated

for word in words: # now for each word in words bank
    if len(word) ==  0:  # if the length of the word is 0 then 
        translated_words.append(word) # just append the word into the translated_words list 
        continue 
    ''' This immediately jumps to the next iteration of the loop,
    skipping the rest of the code within the loop body for that particular word. '''
    first_letter= word[0] # if the words has more characters then this start to execute as the first_letter will become the word[0]
    rest_of_word =word[1:] # remaining letters of the same word starting from the second letter gets into rest_of_word
    translated_word = rest_of_word + first_letter + "ay" '''according to the translated word for our pig_latin then we can 
    say that rest_of_word comes first then the first letter of the same word and adding "ay" at the end.'''
    translated_words.append(translated_word) # then we will append each word into the translated_words list one by one
translated_story = " ".join(translated_words) # then we are forming the translated story by using all the transaltedd words using join keyword 
print(translated_story) # Cool we will print that translated story 


