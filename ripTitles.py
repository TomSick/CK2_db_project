import json
import os

# Method to populate titles json with files in the titles folder.


def title_rip(filepath):
    titles = {}
    for filename in os.listdir(filepath):
        print(os.path.join(filepath, filename))
        newTitle = filename.strip('.txt')
        titles[newTitle] = {}  # Creates a new title dictionary named after the file opened.
        myfile = open(os.path.join(filepath, filename), encoding='Latin-1')
        # Latin-1 encoding used to prevent errors from non-unicode symbols due to variety of languages.
        for line in myfile:
            if line.strip().startswith('#'):
                continue
            elif line.__contains__('.'):
                year = (line.split('=')[0])
                titles[newTitle][year] = {}  # New dictionaries for each year in a titles file.
            elif line.__contains__('liege'):    # Records if de jure liege changes in given year
                titles[newTitle][year]['liege'] = (line.split('=')[1]).strip('\n')
            elif line.__contains__('holder'):  # Records if the title holder had changed in that year.
                titles[newTitle][year]['holder'] = (line.split('=')[1]).strip('\n')
    with open('titles.json', 'w') as fp:
        json.dump(titles, fp, indent=4)
