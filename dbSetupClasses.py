import json
import sqlite3
connection = sqlite3.connect('start.db')
cursor = connection.cursor()


def import_dynasties(path):
    with open(path) as f:
        dynInfo = json.load(f)
        cursor.execute("DROP TABLE IF EXISTS dynasties")
        cursor.execute("CREATE TABLE dynasties (dynastyID PRIMARY KEY, surname)")
        for key in dynInfo:
            cursor.execute("INSERT INTO dynasties (dynastyID, surname) VALUES (?, ?)", (key, dynInfo[key]['name']))
    connection.commit()


def import_characters(path):
    with open(path) as f:
        charInfo = json.load(f)
    cursor.execute('DROP TABLE IF EXISTS characters')
    cursor.execute("CREATE TABLE characters (charid PRIMARY KEY, name, dynasty, religion, culture)")
    for key in charInfo:
        cursor.execute("INSERT INTO characters (charid, name, dynasty, religion, culture) VALUES (?, ?, ?, ?, ?)", (key, charInfo[key]['name'], charInfo[key]['dynasty'], charInfo[key]['religion'], charInfo[key]['culture']))

    connection.commit()


def import_titles(path):
    with open(path) as f:
        titInfo = json.load(f)

    cursor.execute("DROP TABLE IF EXISTS titles")
    cursor.execute("CREATE TABLE titles (titID PRIMARY KEY, holding, level)")
    for key in titInfo:
        if key.startswith('c'):
            lvl = 'County'
        elif key.startswith('d'):
            lvl = 'Duchy'
        elif key.startswith('K'):
            lvl = 'Kingdom'
        elif key.startswith('E'):
            lvl = 'Empire'
        holding = (key.split('_')[1]).split(':')[0]
        cursor.execute("INSERT INTO titles (titID, holding, level) VALUES (?, ?, ?)", (key, holding, lvl))

    connection.commit()


def import_title_holders(path):
    with open(path) as f:
        titInfo = json.load(f)
    cursor.execute("DROP TABLE IF EXISTS titleHolders")
    cursor.execute("CREATE TABLE titleHolders (rowIndex INTEGER PRIMARY KEY, title, year, holder)")
    for key in titInfo:
        title = key
        for innerkey in titInfo[key]:
            year = innerkey
            if titInfo[key][innerkey].__contains__('holder'):
                holder = titInfo[key][innerkey]['holder']
                cursor.execute("INSERT INTO titleHolders (title, year, holder) VALUES (?, ?, ?)", (title, year, holder))

    connection.commit()
