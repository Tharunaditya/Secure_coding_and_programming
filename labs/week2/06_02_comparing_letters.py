# can you figure out the logic here?

ay = "a"
bee = "b"

# which one is bigger?

print(ay > bee)

# why??
'''ASCII Values:
ASCII (American Standard Code for Information Interchange) is a character encoding standard
that assigns a unique numerical code to each character. In ASCII, the character 'a' has an ASCII 
value of 97, while 'b' has an ASCII value of 98.   
'''

# here is a hint: check out the ord() function
'''
The ord() function in Python returns the Unicode
code point (often equivalent to the ASCII value) of a given character. 
In this case, ord('a') would return 97, and ord('b') would return 98.
'''
print(ord('a'))
print(ord('b'))

# How does python store string characters under the hood?
'''
Python stores string characters as a sequence of 
Unicode code points. This means that each character
in a string is represented by a unique numerical value, 
which corresponds to a specific character in the Unicode character set.
'''
# look up what ord() does online and report back!
