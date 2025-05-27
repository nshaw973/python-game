from .Color import Color
import random

class Roll:
    # Initialize and check which kind of roll to make
    def __init__(self, rolls, sides):
        self.total = 0
        print(f"Rolling {Color.green(rolls)}d{Color.green(sides)} ")
        if rolls < 2:
            self.total = self.roll_single(sides)
        else:
            self.total = self.roll_mult(self.rolls, self.sides)
        print(f"Total: {Color.yellow(self.total)}")

    # Rolls a single dice
    def roll_single(self, sides):
        result = random.randrange(1,sides)
        return result

    # Rolls multiple dice and returns total
    def roll_mult(self, rolls, sides):
        total = 0
        for i in range(rolls):
            result = self.roll_single(sides)
            print(f"{i+1}. rolled: {result}")
            total += result
        return total
        
    @staticmethod
    # Entity could be a player, npc, enemy, or some sort of envionmental check
    def check_roll(entity, check):
        if entity > check:
            print(f"{Color.green('Passed')} the check!")
            return True
        else:
            print(f"{Color.red('Failed')} the check!")
            return False