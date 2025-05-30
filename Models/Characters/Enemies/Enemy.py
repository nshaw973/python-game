import json
from pathlib import Path
from core import Color
path = Path('lib')

class Enemy:

    with open(f"{path}/enemies.json") as f:
            _ENEMIES_DATA = json.load(f)
    with open(f"{path}/abilities.json") as f:
            _ABILITIES_DATA = json.load(f)

    def __init__(self, enemy_name):
        enemy_data = self._ENEMIES_DATA.get(enemy_name)
        if not enemy_data:
            raise ValueError(f"Enemy '{enemy_name}' not found!")
        
        # Assign stats
        self.name = enemy_data['name']
        self.hp = int(enemy_data['hp'])
        self.defence = int(enemy_data['defence'])
        self.exp = int(enemy_data['exp'])
        self.speed = int(enemy_data['speed'])
        
        # Resolve abilities
        self.abilities = [
            self._ABILITIES_DATA[ability_name] 
            for ability_name in enemy_data["abilities"]
        ]

    def __str__(self):
        return f"Enemy: {self.name} | HP: {self.hp}"