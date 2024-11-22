"""
Use the following commands to look around your directory
You may want to do this exercise interactively with an interpreter session

Path.cwd() gets the current working directory, returns a Path object
os.chdir(path)  changes directory	

os.listdir() files and directories, returns a list
Path.glob(“*”)  returns a generator that you can use to iterate over all files and directories. Advantage is you can filter the results easily on the input.
Path.iterdir()

"""
import os
from pathlib  import Path
def look():
    present_dir = Path.cwd()
    print("Present working directory:",present_dir)
    allfiles = os.listdir()
    print("Files and directories in the current directory:",)
    for item in allfiles:
        print(item)
    pyfiles= Path.cwd().glob("*.py")
    print("The python files prsent here are :")
    for item in pyfiles:
        print(item)
    dir_entries = Path.cwd().iterdir()
    for item in dir_entries:   
        print(dir_entries)

look()