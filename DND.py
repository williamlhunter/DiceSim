import json
from dist_transformer import DiscreteDist

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

class Attack(object):

    def __init__(self, to_hit_bonus, damage_bonus, damage_die, advantage=0):

        hit_roll = DiscreteDist([1/20]*20)
        if advantage == 0:
            hit_roll = 0