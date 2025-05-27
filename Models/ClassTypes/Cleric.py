class Cleric:

    def __init__(self):
        pass

    @staticmethod
    def create():
        return {
        # stats
        'hp': 10,
        'attack': 5,
        'magic': 7,
        'defence': 10,
        'speed': 3,
        # starting equipment
        'weapon': 'mace',
        'armor': 'chain mail',
        'ring': '',
        'pendant': ''
        }