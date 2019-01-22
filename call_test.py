import os
from ripCharacters import name_rip

# This script calls the name_rip method for each file in the character files folder

filepath = 'character files'

for filename in os.listdir(filepath):
    print(os.path.join(filepath, filename))
    ripme = os.path.join(filepath, filename)
    name_rip(ripme)


