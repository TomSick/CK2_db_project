# CK2_db_project
A personal project to create a database of all possible starts in Crusader Kings 2 with a simple web interface. 

This project started when I decided to start a new campaign of Crusader Kings 2. The game offers thousands of possible starting sittuations letting you play as various fuedal lords of Eurasia and Northern Africa over the span of centuries. Despite this huge selection of possible choices though I realized there was no real resource that collected them for players to browse easily.

*Note: At present character stats and traits are not tracked, this will be changed in the future.

## Current status:
* Python to extract information to json format completed
* Python to export json files to SQLite database completed

## Use:

### Building a local database
To build a local database locate the necessary files by navigating to the history folder in the games install directory. From the history folder copy the characters and titles folders to this programs '\source file directory' confirming any replacments. The default location for steam installations will be C:\SteamLibrary\steamapps\common\Crusader Kings II\history

Next we have one more file to grab, locate the 00_dynasties.txt file in the 'Crusader Kings II\common\dynasties' folder and copy this file to the same location as the previous files once again replacing the existing file if prompted.

Run PopulateJSON.py to import the info from the source files and export them to JSON.

Run setupDB.py to import info from the JSON files and export the data to a local SQLite database. This will create the database if it does not yet exist, or update it if already existing.
