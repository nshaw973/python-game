import json
import random
from pathlib import Path
map_path = Path("lib")
from core import Color, Roll ,user_input
from Models import Enemy

def load_map(player, dungeon_file):
    with open(f"{map_path}/{dungeon_file}.json", 'r') as f:
        dungeon = json.load(f)
    if dungeon:
        print(f"{player['name']} has entered the {dungeon['name']}!")
    enemies = dungeon['enemies']

def floor_event(player, enemies):
    # Get Enemy Data
    total_enemies = []
    rand_enemy = random.randrange(0,len(enemies))
    enemy = Enemy(rand_enemy)
    quantity = random.randrange(1,3)
    for i in range(quantity):
        total_enemies.append(enemy)
    # Initiatives
    player_initiative = Roll(1,20).total + player['speed']
    # Turns
    current_turn = 1
    