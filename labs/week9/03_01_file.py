"""
use a context manager to open the file winnie_pooh.txt

try it two ways
a) make a Path object that points to winnie_pooh.txt
b) just write it in as a string (don't use a Path object)

Both are valid! The first method is the OO way and will yield better programs down the line.
The second way is fine for quick scripts though

## Tasks to try
1. Print out of the first line of the file
2. Print out all the entire file
3. Print in the last line of the file
4. Add a new sentence to the file "I AM A NEW SENTENCE!"
5. 

"""

from pathlib import Path
file_path = Path("winnie_pooh.txt")
# 1. Print out of the first line of the file
with file_path.open("r") as file:
    first_line = file.readline()
    print("First Line:", first_line.strip())
#2. Print out all the entire file
with file_path.open("r") as file:
    content = file.read()
    print("Entire File:\n", content)
#3. Print in the last line of the file
with file_path.open("r") as file:
    lines = file.readlines()  
    last_line = lines[-1].strip() 
    print("Last Line:", last_line)
# 4. Add a new sentence to the file "I AM A NEW SENTENCE!"
with file_path.open("a") as file:  
    file.write("\nI AM A NEW SENTENCE!")
    print("Appended a new sentence!")
