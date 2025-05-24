import json
from pathlib import Path
save_path = Path('game/save')
# Color Decoration for text
from Models.Other.Color import Color
# Archetype Models
from Models.ClassTypes.Mage import Mage
from Models.ClassTypes.Fighter import Fighter
from Models.ClassTypes.Rogue import Rogue
from Models.ClassTypes.Cleric import Cleric

class Player:

    def __init__(self):     
        # --- Name Selection ---
        while True:
            print(f"What is your character's {Color.red('NAME')}?\n(8 Characters Max):")
            name = input(Color.blue('>>> ')).strip
            
            if not (1 <= len(name) <= 8):
                print("Name must be between 1 and 8 characters")
                continue
                
            if not name.isalpha():
                print("Cannot have special characters or numbers!")
                continue

            self.name = name.capitalize()
            break
        
        # --- Class Selection ---
        classes = {
            'fighter': Fighter.stats(),
            'mage': Mage.stats(),
            'rogue': Rogue.stats(),
            'cleric': Cleric.stats()
        }
        
        while True:
            c_class = input(f"Choose a class:\n{Color.red('1. Fighter')}\n{Color.cyan('2. Mage')}\n{Color.green('3. Rogue')}\n{Color.yellow('4. Cleric')}\n> ")
            c_class = input(Color.blue('>>> ')).strip().lower()
            if c_class not in classes:
                print(Color.red("Please input one of the provided classes."))
                continue
            
            self.c_class = c_class.capitalize()
            stats = classes[c_class]
            
            # Assign stats
            self.level = 1
            self.hp = stats["hp"]
            self.attack = stats["attack"]
            self.magic = stats["magic"]
            self.defence = stats["defence"]
            self.speed = stats["speed"]
            break
        
        print(f"\nCharacter created: {self.name} the {self.c_class}")
        print(f"Stats:\nHP={self.hp}\nATK={self.attack}\nMAG={self.magic}\nDEF={self.defence}\nSPD={self.speed}")

    # Convert player into json file.
    def to_dict(self):
        return {
            "name": self.name,
            "class": self.c_class,
            "level": self.level,
            "stats": {
                "hp": self.hp,
                "attack": self.attack,
                "magic": self.magic,
                "defence": self.defence,
                "speed": self.speed
            },
            "equipment": {
                "weapon": "",
                "armor": "",
                "ring": "",
                "pendant": "",
            },
            "inventory": {}
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