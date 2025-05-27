class Fighter:
    
    def __init__(self):
        pass

    @staticmethod
    def create():
        return {
        # stats
        'hp': 10,
        'attack': 12,
        'magic': 1,
        'defence': 7,
        'speed': 5,
        # starting equipment
        'weapon': 'shortsword',
        'armor': 'chain shirt',
        'ring': '',
        'pendant': ''
        }