"""
Use pathlib.Path objects to 

a) create a new directory
b) create a new file
c) move a file from your current directory into the new directory

use shutil to
d) copy the file back into the original location (while keeping it in the new directory)

"""


from pathlib import Path
import shutil

# a) Create a new directory
new_dir = Path("new_directory")
new_dir.mkdir(exist_ok=True)  # Create the directory if it doesn't exist

# b) Create a new file
new_file = new_dir / "new_file.txt"
new_file.touch()  # Create the file

# c) Move the file into the new directory
original_file = Path("original_file.txt")
original_file.replace(new_file)  # Move the file

# d) Copy the file back to the original location (keeping it in the new directory)
shutil.copy(new_file, original_file)  # Copy the file