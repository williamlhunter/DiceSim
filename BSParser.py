import xmltodict
import re

#contains stats for each unit and weapon for a race, each in it's own dictionary
class Race(object):

    def __init__(self, race):
        self.units = {}
        self.weapons = {}
        self.models = {}
        try:
            with open('/Users/billhunter/OneDrive/Code/KTData/wh40k-killteam/' + race + '.cat') as data_file:
                raw = xmltodict.parse(data_file.read(), force_list=('profile'))
        except:
            print(race + " does not exist.")
            return

        selection_entries = raw['catalogue']['sharedSelectionEntries']['selectionEntry']
        
        for entry in selection_entries:
            if entry['@type'] == 'unit':
                self.units[entry['@name']] = entry
            elif entry['@type'] == 'upgrade':
                self.weapons[entry['@name']] = Weapon(entry)
            elif entry['@type'] == 'model':
                self.models[entry['@name']] = Model(entry)
        

#represents the relevant parts of a model for KillTeam
class Model(object):

    def __init__(self, selection_entry):
        self.stats = {}
        self.stats['PTS'] = int(float(selection_entry['costs']['cost']['@value']))
        for e in selection_entry['profiles']['profile'][0]['characteristics']['characteristic']:
            try:
                self.stats[e['@name']] = int(re.findall(r'\d+', e['#text'])[0])
            except Exception as x:
                self.stats[e['@name']] = 0
    
    def __str__(self):
        return str(self.stats)

class Weapon(object):

    def __init__(self, selection_entry):
        self.stats = {}
        self.stats['PTS'] = int(float(selection_entry['costs']['cost']['@value']))
        for e in selection_entry['profiles']['profile'][0]['characteristics']['characteristic']:
            name = e['@name']
            if name == 'Type' or name == 'Abilities':
                self.stats[name] = e['#text']
            else:
                try:
                    self.stats[name] = int(re.findall(r'\d+', e['#text'])[0])
                except:
                    self.stats[e['@name']] = 0
    
    def __str__(self):
        return str(self.stats)