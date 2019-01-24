import json
import re

# Method to populate dynasty json with info from dynasties text file.


def dynasty_rip(filepath):
    dynasties = {}
    pattern = r"^(\d)"
    myfile = open(filepath, encoding='Latin-1')
    for line in myfile:
        if line.startswith('#'):
            continue
        elif re.match(pattern, line) and line.__contains__('='):
            dynasty = (line.split('=')[0])
            dynasties[dynasty] = {}
        elif line.__contains__('name'):
            dynasties[dynasty]['name'] = (line.split('=')[1]).strip('\n')
    print(dynasties)
    with open('dynasties.json', 'w') as fp:
        json.dump(dynasties, fp, indent=4)