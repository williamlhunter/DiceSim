import xmltodict
import re

#contains stats for each unit and weapon for a race, each in it's own dictionary
class KTRace(object):

    def __init__(self, race):
        self.units = {}
        self.upgrades = {}
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
                self.upgrades[entry['@name']] = entry
            elif entry['@type'] == 'model':
                self.models[entry['@name']] = KTModel(entry)
        

#represents the relevant parts of a model for KillTeam
class KTModel(object):

    stat_names = ['M', 'WS', 'BS', 'S', 'T', 'W', 'A', 'LD', 'SV', 'MAX']

    def __init__(self, selection_entry):
        self.stats = {}
        self.stats['cost'] = int(float(selection_entry['costs']['cost']['@value']))
        for e in selection_entry['profiles']['profile'][0]['characteristics']['characteristic']:
            try:
                self.stats[e['@name']] = int(re.findall(r'\d+', e['#text'])[0])
            except Exception as x:
                self.stats[e['@name']] = 0
    
    def __str__(self):
        return str(self.stats)