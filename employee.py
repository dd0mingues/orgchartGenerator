import json
import random

class employee:
    def __init__(self, manager=None):
        if manager:
            self.level = manager.level +1
            self.manager = manager.email
            
        else:
            self.level = 1
            self.manager = manager
        
        self.id = random.randint(100000000, 999999999)
        self.fName = generate_random_name()
        self.lName = generate_random_name()
        self.email = f"{self.fName.lower()}.{self.lName.lower()}@example.com"
        self.nrSub = 0
        self.toolTip = "Employee"
    
# List of syllables to form names
syllables = ['ba', 'be', 'bi', 'bo', 'bu',
             'da', 'de', 'di', 'do', 'du',
             'ga', 'ge', 'gi', 'go', 'gu',
             'ka', 'ke', 'ki', 'ko', 'ku',
             'la', 'le', 'li', 'lo', 'lu',
             'ma', 'me', 'mi', 'mo', 'mu',
             'na', 'ne', 'ni', 'no', 'nu',
             'pa', 'pe', 'pi', 'po', 'pu',
             'ra', 're', 'ri', 'ro', 'ru',
             'sa', 'se', 'si', 'so', 'su',
             'ta', 'te', 'ti', 'to', 'tu',
             'va', 've', 'vi', 'vo', 'vu',
             'za', 'ze', 'zi', 'zo', 'zu']

# Generate random names
def generate_random_name():
    name = ''
    # Randomly select number of syllables in the name (between 2 and 4)
    num_syllables = random.randint(2, 4)
    for _ in range(num_syllables):
        # Randomly select a syllable and add it to the name
        name += random.choice(syllables).capitalize()
    return name

class EmployeeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, employee):
            return obj.__dict__
        return json.JSONEncoder.default(self, obj)