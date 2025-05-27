from .Color import Color
import random

class Roll:
    # Type of dice available / sides
    # 2 is a coinflip
    dice_types = (2, 4, 6, 8, 10, 12, 20, 100)
    # Initialize and check which kind of roll to make
    def __init__(self, rolls, sides):
        self.total = 0
        print(f"Rolling {Color.green(rolls)}d{Color.green(sides)} ")
        if rolls < 2:
            self.total = self.roll_single(sides)
        else:
            self.total = self.roll_mult(rolls, sides)
        print(f"Total: {Color.yellow(str(self.total))}")

    # Rolls a single dice
    def roll_single(self, sides):
        result = random.randrange(1,sides)
        return int(result)

    # Rolls multiple dice and returns total
    def roll_mult(self, rolls, sides):
        total = 0
        for i in range(rolls):
            result = self.roll_single(sides)
            print(f"{i+1}. rolled: {result}")
            total += result
        return int(total)
        
    @staticmethod
    # Entity could be a player, npc, enemy, or some sort of envionmental check
    def check_roll(entity, check):
        if entity > check:
            print(f"{Color.green('Passed')} the check!")
            return True
        else:
            print(f"{Color.red('Failed')} the check!")
            return False