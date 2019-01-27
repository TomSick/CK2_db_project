import json
import re
import os

# Class to populate characters json with files in the characters folder.


def name_rip(filepath):
    lords = {}
    pattern = r"^(\d)+"  # Starts with repeating digits
    for filename in os.listdir(filepath):
        # print(os.path.join(filepath, filename))
        myfile = open(os.path.join(filepath, filename), encoding='Latin-1')
        # Latin-1 encoding used to avoid errors from non unicode characters in names
        for line in myfile:
            if line.startswith('#'):  # Skips commented out characters
                continue
            elif re.match(pattern, line) and not line.__contains__('.'):  # Not rule avoids grabbing dates
                newlord = (line.split('=')[0]).strip()
                lords[newlord] = {}  # New dictionary from charID
            elif line.__contains__('name=') or line.__contains__('name ='):
                if line.__contains__('#'):
                    lords[newlord]['name'] = ((line.split('=')[1]).split('#')[0]).strip('\n')
                else:
                    lords[newlord]['name'] = (line.split('=')[1]).strip('\n')
            elif line.__contains__('dynasty=') or line.__contains__('dynasty ='):
                if line.__contains__('#'):
                    lords[newlord]['dynasty'] = ((line.split('=')[1]).split('#')[0]).strip('\n')
                else:
                    lords[newlord]['dynasty'] = (line.split('=')[1]).strip('\n')
            elif line.__contains__('religion=') or line.__contains__('religion ='):
                if line.__contains__('#'):
                    lords[newlord]['religion'] = ((line.split('=')[1]).split('#')[0]).strip('\n')
                else:
                    lords[newlord]['religion'] = (line.split('=')[1]).strip('\n')
            elif line.__contains__('culture=') or line.__contains__('culture ='):
                if line.__contains__('#'):
                    lords[newlord]['culture'] = ((line.split('=')[1]).split('#')[0]).strip('\n')
                else:
                    lords[newlord]['culture'] = (line.split('=')[1]).strip('\n')
            if not lords[newlord].__contains__('dynasty'):
                lords[newlord]['dynasty'] = '0';
            if not lords[newlord].__contains__('culture'):
                lords[newlord]['culture'] = '0';
            if not lords[newlord].__contains__('name'):
                lords[newlord]['name'] = 'who?';

    with open('json/characters.json', 'w') as fp:
        json.dump(lords, fp, indent=4)

    print('character rip complete')
