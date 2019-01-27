import json
import re

# Class to populate dynasty json with info from dynasties text file.


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
            if line.__contains__('#'):
                dynasties[dynasty]['name'] = ((line.split('=')[1]).split('#')[0]).strip('\n')  # .strip('\"')
            else:
                dynasties[dynasty]['name'] = (line.split('=')[1]).strip('\n').strip('\"')
    # print(dynasties)
    with open('json/dynasties.json', 'w') as fp:
        json.dump(dynasties, fp, indent=4)

    print('dynasty rip complete')
