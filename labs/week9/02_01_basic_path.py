"""
Let's make a very basic Path object

"""

from pathlib import Path

##
cwd = Path.cwd()

print(cwd)
## create a new path using concatenation
new_path = cwd /"new_folder"/"my_file.txt"
# you can use cwd.joinpath
# or you can use the special / symbol (overloaded for concatenation)


## examine your new path object

## print the following parts

# .parent
print("Parent directory:", new_path.parent)
# .anchor
print("Anchor (root):", new_path.anchor)
# .name
print("Name (basename):", new_path.name)
# .stem
print("Stem (filename without extension):", new_path.stem)
# .suffix
print("Suffix (file extension):", new_path.suffix)
# .parent
print("Parent directory:", new_path.parent)

## check if your path is a directory or file

## .is_file()

## .is_dir()
print("Is it a file?", new_path.is_file())  # This will be False as we haven't created the file yet
print("Is it a directory?", new_path.is_dir())  # This will also be False initially

## print out your path and look at the type (you may need to print(type(your_path_here)))
## does it accurately reflect your OS?
print("Path:", new_path)
print("Type:", type(new_path))

