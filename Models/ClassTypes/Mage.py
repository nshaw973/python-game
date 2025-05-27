class Mage:

    def __init__(self):
        pass

    @staticmethod
    def create():
        return {
        # stats
        'hp': 10,
        'attack': 3,
        'magic': 12,
        'defence': 3,
        'speed': 7,
        # starting equipment
        'weapon': 'quarterstaff',
        'armor': 'robe',
        'ring': '',
        'pendant': ''
        }