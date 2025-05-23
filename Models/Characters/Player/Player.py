import json
from pathlib import Path
save_path = Path('game/save')

class Player:
    CLASS_STATS = {
        "fighter": {"hp": 13, "attack": 10, "magic": 1, "defence": 7, "speed": 3},
        "mage": {"hp": 7, "attack": 1, "magic": 10, "defence": 4, "speed": 5},
        "rogue": {"hp": 7, "attack": 13, "magic": 3, "defence": 5, "speed": 8},
        "cleric": {"hp": 15, "attack": 4, "magic": 8, "defence": 10, "speed": 3}
    }
    
    def __init__(self):
            self.get_name()
            self.get_class()
            self.set_class_stats()

    def get_name(self):
        while True:
            name = input("What is your character's name?\n(8 Characters Max): ").strip()
                
            if not (1 <= len(name) <= 8):
                print("Name must be between 1 and 8 characters")
                continue
                    
            if not name.isalpha():
                print("Cannot have special characters or numbers!")
                continue

            self.name = name.capitalize()
            break
    
    def get_class(self):
        classes = ["fighter", "mage", "rogue", "cleric"]
        while True:
            c_class = input("Choose a class:\nFighter\nMage\nRogue\nCleric\n> ").strip().lower()
            if c_class not in classes:
                print("Please input one of the provided classes.")
                continue
            self.c_class = c_class.capitalize()
            break
        
    def set_class_stats(self):
        """Set stats based on class using the CLASS_STATS dictionary"""
        stats = self.CLASS_STATS.get(self.c_class, {
            "hp": 10,
            "attack": 5,
            "magic": 5,
            "defence": 5,
            "speed": 5
        })
        self.hp = stats["hp"]
        self.attack = stats["attack"]
        self.magic = stats["magic"]
        self.defence = stats["defence"]
        self.speed = stats["speed"]
    
    def to_dict(self):
        """Convert player data to dictionary for JSON serialization"""
        return {
            "name": self.name,
            "class": self.c_class,
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
    
    def save_to_file(self, filename):
        """Save player data to JSON file"""
        with open(f"{save_path}/{filename}.json", 'w') as f:
            json.dump(self.to_dict(), f, indent=4)

    @classmethod
    def load_from_file(cls, filename):
        """Load player data from JSON file"""
        with open(f"{save_path}/{filename}.json", 'r') as f:
            data = json.load(f)
            return data