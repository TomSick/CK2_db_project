import dbSetupClasses

# This file calls the classes used to populated the database.

#  JSON file locations
dynasty = 'json/dynasties.json'
character = 'json/characters.json'
title = 'json/titles.json'

dbSetupClasses.import_dynasties(dynasty)

dbSetupClasses.import_characters(character)

dbSetupClasses.import_titles(title)

dbSetupClasses.import_title_holders(title)
