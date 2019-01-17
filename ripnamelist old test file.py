import json

myfile = open('test.txt')

lords = {}

for line in myfile:
    if line.__contains__(' = {') and not line.__contains__('.'):
        newlord = line.split(' ')[0]
        lords[newlord] = {}
    elif line.__contains__('name='):
        lords[newlord]['name'] = (line.split('=')[1]).strip('\n')
    elif line.__contains__('dynasty1='):
        lords[newlord]['dynasty'] = (line.split('=')[1]).strip('\n')
    elif line.__contains__('religion='):
        lords[newlord]['religion'] = (line.split('=')[1]).strip('\n')
    elif line.__contains__('culture='):
        lords[newlord]['culture'] = (line.split('=')[1]).strip('\n')

    elif line == '\n':
        print('I can find new lines')


print(lords)

with open('outfile.json', 'w') as fp:
    json.dump(lords,fp,indent=4)

myfile.close()
