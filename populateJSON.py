from ripCharacters import name_rip
from ripTitles import title_rip
from ripDynasties import dynasty_rip

# This file serves to call the two methods needed to populate the jsons.

characterFilePath = 'source files/character files'  # Subdirectory where character files are located.

titleFilePath = 'source files/titles'  # Subdirectory where title files are located.

dynastyFilePath = 'source files/00_dynasties.txt'  # Location of dynasties text file

name_rip(characterFilePath)
title_rip(titleFilePath)
dynasty_rip(dynastyFilePath)
