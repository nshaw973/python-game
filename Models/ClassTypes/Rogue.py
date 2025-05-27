class Rogue:

    def __init__(self):
        pass

    @staticmethod
    def create():
        return {
        # stats
        'hp': 10,
        'attack': 7,
        'magic': 3,
        'defence': 5,
        'speed': 10,
        # starting equipment
        'weapon': 'dagger',
        'armor': 'leather',
        'ring': '',
        'pendant': ''
        }