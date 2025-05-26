import json
from pathlib import Path
save_path = Path('game/save')
# Utilities
from core import user_input, Color
# Archetype Models
from Models import Mage, Fighter, Rogue, Cleric

class Player:

    def __init__(self):     
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
        
        # --- Class Selection ---
        classes = {
            'fighter': Fighter.stats(),
            'mage': Mage.stats(),
            'rogue': Rogue.stats(),
            'cleric': Cleric.stats()
        }
        
            # Different Available Classes
        archetypes = ('fighter', 'mage', 'rogue', 'cleric')
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
            
            class_index = int(choice) - 1  # Convert to 0-based index
            self.archetype = archetypes[class_index]
            stats = classes[self.archetype]
            
            # Assign stats
            self.level = 1
            self.hp = stats["hp"]
            self.attack = stats["attack"]
            self.magic = stats["magic"]
            self.defence = stats["defence"]
            self.speed = stats["speed"]
            break
        
        print(f"\nCharacter created: {self.name} the {Color.get_class_color(self.archetype)}")
        print(f"Stats:\nHP={self.hp}\nATK={self.attack}\nMAG={self.magic}\nDEF={self.defence}\nSPD={self.speed}")

    # Convert player into json file.
    def to_dict(self):
        return {
            "name": self.name,
            "class": self.archetype,
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