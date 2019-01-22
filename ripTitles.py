import json
import os

filepath = 'test files'

titles = {}

for filename in os.listdir(filepath):
    print(os.path.join(filepath, filename))
    newTitle = filename.strip('.txt')
    titles[newTitle] = {}
    myfile = open(os.path.join(filepath, filename))

    for line in myfile:
        if line.startswith('#'):
            continue
        elif line.__contains__('.'):
            year = (line.split('=')[0])
            titles[newTitle][year] = {}
        elif line.__contains__('liege'):
            titles[newTitle][year]['liege'] = (line.split('=')[1]).strip('\n')
        elif line.__contains__('holder'):
            titles[newTitle][year]['holder'] = (line.split('=')[1]).strip('\n')

print(titles)
with open('titles.json', 'w') as fp:
    json.dump(titles, fp, indent=4)
