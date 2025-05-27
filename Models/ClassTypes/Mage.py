from core import Roll

class Mage:
    def __init__(self):
        pass

    @staticmethod
    def get_stats():
        return {
            'hp': 10,
            'attack': 5,
            'magic': 7,
            'defence': 10,
            'speed': 3,
            'weapon': 'mace',
            'armor': 'chainmail',
            'ring': '',
            'pendant': ''
        }

    def level_up_rolls(self):
        return {
            'hp': Roll(1,6).total,
            'attack': Roll(1,6).total,
            'magic': Roll(1,8).total,
            'defence': Roll(1,8).total,
            'speed': Roll(1,4).total,
        }