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
        """Lightning-fast lookup by name (no searching)."""
        enemy_stats = self._ENEMIES_DATA.get(enemy_name)
        if not enemy_stats:
            raise ValueError(f"Enemy '{enemy_name}' not found!")
        
        # Assign stats
        self.name = enemy_name
        self.health = enemy_stats["health"]
        self.attack = enemy_stats.get("attack", 0)
        
        # Resolve abilities
        self.abilities = [
            self._ABILITIES_DATA[ability_name] 
            for ability_name in enemy_stats["abilities"]
        ]