import json
from pathlib import Path
save_path = Path('game/save')
# Utilities
from core import user_input, Color
# Archetype Models
from Models import Mage, Fighter, Rogue, Cleric

classes = {
            'fighter': Fighter(),
            'mage': Mage(),
            'rogue': Rogue(),
            'cleric': Cleric()
        }
class_list = list(classes.keys())
attributes = ['hp', 'attack', 'magic', 'defence', 'speed', 
              'weapon', 'armor', 'ring', 'pendant']
class Player:
    def __init__(self):
        # --- Data ---
        self.level = 1
        self.archetype = ''
        self.hp = 0
        self.attack = 0
        self.magic = 0
        self.defence = 0
        self.speed = 0   
        self.weapon = ''
        self.armor = ''
        self.ring = ''
        self.pendant = ''
        self.inventory = []
        # --- Name Selection ---
        while True:
            print(f"What is your character's {Color.red('NAME')}?\n(8 Characters Max):")
            name = user_input()
            
            if not (1 <= len(name) <= 8):
                print("Name must be between 1 and 8 characters")
                continue
                
            if not name.isalpha():
                print("Cannot have special characters or numbers!")
                continue

            self.name = name.capitalize()
            break
        # Choose
        while True:
            print(f"Choose a class (1-4):\n"
                f"{Color.red('1. Fighter')}\n"
                f"{Color.cyan('2. Mage')}\n"
                f"{Color.green('3. Rogue')}\n"
                f"{Color.yellow('4. Cleric')}")
            
            choice = user_input()
            if not choice.isdigit() or not (1 <= int(choice) <= 4):
                print(Color.red("Please enter a number between 1-4."))
                continue
            
            class_index = int(choice) - 1
            self.archetype = class_list[class_index]
            data = classes[self.archetype].get_stats()

            self.level = 1
            self.__dict__.update(data)  # Assigns all stats at once
            break
        
    # Level up player based on chosen class
    @classmethod
    def level_up(cls, player):
        data = classes[player['archetype']].level_up_rolls()
        player['level'] += 1
        print(f"Congrats! {player['name']} is now level {player['level']}!")
        
        # Single loop to update all stats
        for stat, value in data.items():
            player['stats'][stat] += value
        
        return player

    # Convert player into json file.
    def to_dict(self):
        return {
            "name": self.name,
            "archetype": self.archetype,
            "level": self.level,
            "stats": {
                "hp": self.hp,
                "attack": self.attack,
                "magic": self.magic,
                "defence": self.defence,
                "speed": self.speed
            },
            "equipment": {
                "weapon": self.weapon,
                "armor": self.armor,
                "ring": self.ring,
                "pendant": self.pendant,
            },
            "inventory": []
        }
    
    def save_to_file(self):
        # Save player to json file
        with open(f"{save_path}/{self.name}.json", 'w') as f:
            json.dump(self.to_dict(), f, indent=4)

    @classmethod
    def load_from_file(cls, filename):
        # Load player from json file
        with open(f"{save_path}/{filename}.json", 'r') as f:
            data = json.load(f)
            return data