import sqlite3
import json

connection = sqlite3.connect('start.db')
cursor = connection.cursor()

with open('characters.json') as f:
    data = json.load(f)

for key in data:
    print(key)

#
# titleID = 1
# titleName = 'Tim'
#
# cursor.execute('Create Table Titles (titleID INTEGER PRIMARY KEY, title TEXT)')
#
# cursor.execute('INSERT INTO titles VALUES(?,?)'), (titleID, titleName)
#
#
#
# For dictionary in json:
#     create table (Dic name)
#         column year
#         column title holder
#             For attribute in dictionary
#                 write row
#
# for dictionary in json
#     create table
#         column year
#         column liege
#             For attribute in dictionary
#                 write row