import json

class Data(object):

    def __init__(self):
        with open('/Users/billhunter/OneDrive/Code/5e-database/5e-SRD-Monsters.json') as data_file:
            raw_monsters = json.loads(data_file.read())
        with open('/Users/billhunter/OneDrive/Code/5e-database/5e-SRD-Races.json') as data_file:
            raw_races = json.loads(data_file.read())
        with open('/Users/billhunter/OneDrive/Code/5e-database/5e-SRD-Classes.json') as data_file:
            raw_classes = json.loads(data_file.read())
        with open('/Users/billhunter/OneDrive/Code/5e-database/5e-SRD-Equipment.json') as data_file:
            raw_equipment = json.loads(data_file.read())
        
        self.monsters = {}
        for item in raw_monsters:
            self.monsters[item['name']] = item


db = Data()
print(db.monsters['Wolf'])