"""

Create two new folders
a. vowel
b. consonant

Iterate over your previously created files from 04_04_split_file.py
Open each file and check if the first word begins in a vowel or consonant
If it begins in a vowel, move the file to the vowel folder
Otherwise move the file to the consonant folder

"""

import os
import shutil
from string import vowels

def sort_files_by_first_word(directory, vowel, consonant):
    os.makedirs(vowel, exist_ok=True)
    os.makedirs(consonant, exist_ok=True)

    for filename in os.listdir(directory):
        if filename.startswith('.'):
            continue

        filepath = os.path.join(directory, filename)
        with open(filepath, 'r') as file:
            first_word = file.readline().strip().split()[0].lower()

        destination_folder = vowel if first_word[0] in vowels else consonant
        shutil.move(filepath, os.path.join(destination_folder, filename))

if __name__ == '__main__':
    directory = "./week9/splited_files"
    vowel = "vowel"
    consonant = "consonant"

    sort_files_by_first_word(directory, vowel, consonant)