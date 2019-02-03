# CK2_db_project
A personal project to create a database of all possible starts in Crusader Kings 2 with a simple web interface. 

This project started when I decided to start a new campaign of Crusader Kings 2. The game offers thousands of possible starting sittuations letting you play as various fuedal lords of Eurasia and Northern Africa over the span of centuries. Despite this huge selection of possible choices though I realized there was no real resource that collected them for players to browse easily.

*Note: At present character stats and traits are not tracked, this will be changed in the future.

## Current status:
* Python to extract information to json format completed
* Python to export json files to SQLite database completed

## Use:

###Building a local database
To build a local database locate the necessary files navigate to the history folder in the games install directory. From the history folder copy the characters and titles folders to this programs '\source file directory' confirming any replacments. The default location for steam installations will be C:\SteamLibrary\steamapps\common\Crusader Kings II\history

Next we need to grab one more file to grab, locate the 00_dynasties.txt file in the Crusader Kings II\common\dynasties
Move this file to the source to the same location and once again replace the existing file if asked.

Run PopulateJSON.py to extract the info from the game files to JSON.

Run setupDB.py to create your database from the JSON files.
