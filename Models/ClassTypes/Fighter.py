class Fighter:
    
    def __init__(self):
        pass

    @staticmethod
    def stats():
        return {
        'hp': 13,
        'attack': 10,
        'magic': 1,
        'defence': 7,
        'speed': 3,
        }
    
    @staticmethod
    def starting_equipment():
        return {
            'weapon': 'sword',
            'armor': 'chain shirt',
            'ring': '',
            'pendant': ''
        }