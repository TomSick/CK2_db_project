import json
import re

# This method is designed to populate a json with the information stored in the character files folder.
# The method first runs a loop to populate a dictionary called lords with the desired information.
def name_rip(str):
    myfile = open(str, encoding='Latin-1')
    lords = {}
    pattern = r"^(\d)+"

    for line in myfile:
        # if line.__contains__(' = {') and not line.__contains__('.'):
        if line.startswith('#'):
            continue
        elif re.match(pattern, line) and not line.__contains__('.'):
            newlord = line.split(' ')[0]
            lords[newlord] = {}
        elif line.__contains__('name=') or line.__contains__('name ='):
            lords[newlord]['name'] = (line.split('=')[1]).strip('\n')
        elif line.__contains__('dynasty=') or line.__contains__('dynasty ='):
            lords[newlord]['dynasty'] = (line.split('=')[1]).strip('\n')
        elif line.__contains__('religion=') or line.__contains__('religion ='):
            lords[newlord]['religion'] = (line.split('=')[1]).strip('\n')
        elif line.__contains__('culture=') or line.__contains__('culture ='):
            lords[newlord]['culture'] = (line.split('=')[1]).strip('\n')

    print(lords)  # Prints parsed data for confirmation and troubleshooting.

    with open('characters.json') as fp:
        data = json.load(fp)
        data.update(lords)
    with open('characters.json', 'w') as fp:
        json.dump(data,fp,indent=4)

        # The characters json is loaded and it's value assigned to a dictionary.
        # Using the update() method that dictionary is then updated with the contents of lords.
        # Any keys from the lords dictionary not already in the data dictionary are added while others are updated.
        # The updated dictionary is then dumped to json.