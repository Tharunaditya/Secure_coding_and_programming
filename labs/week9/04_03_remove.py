"""
CAUTION
Deleting anything with python will permanently delete the file!
You will not be able to recover anything you delete with python!
USE CAUTION!
CAUTION

Use Path.rmdir() and Path.unlink() to delete a folder and file respectively

"""
from pathlib import Path

directory_to_delete = Path("")
if directory_to_delete.exists():
    directory_to_delete.rmdir()
    print(f"Directory '{directory_to_delete}' deleted successfully.")
else:
    print(f"Directory '{directory_to_delete}' does not exist.")
    


file_to_delete = Path("")
if file_to_delete.exists():
    file_to_delete.unlink()
    print(f"File '{file_to_delete}' deleted successfully.")
else:
    print(f"File '{file_to_delete}' does not exist.")