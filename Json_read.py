import json

with open('data.txt') as jsonf:  
    data = json.load(jsonf)
    print(data)
    print()
    for p in data['people']:
        print('Name: ' + p['name'])
        print('Website: ' + p['website'])
        print('From: ' + p['from'])
        print('')
