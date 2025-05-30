import json
import random
from pathlib import Path
map_path = Path("lib/maps")
from core import Color, Roll ,user_input, top_break, bottom_break
from Models import Enemy

def load_map(player, dungeon_file):
    with open(f"{map_path}/{dungeon_file}.json", 'r') as f:
        dungeon = json.load(f)
    if dungeon:
        print(f"{player['name']} has entered the {dungeon['name']}!")
    enemies = dungeon['enemies']
    # Run through floors
    current_floor = 1
    while current_floor < dungeon['floors']:
        top_break(Color.random(dungeon['name']))
        print(f"Current Floor: {current_floor}")
        run_floor = floor_event(player, enemies)
        if run_floor:
            print("Moving to next Floor")
            current_floor += 1
            continue
        else:
            print(f"Ran from floor {current_floor}")
            break
    
def floor_event(player, enemies):
    # Get Player Data
    player_stats = player['stats']
    # Get Enemy Data
    total_enemies = []
    rand_enemy = random.randrange(0,len(enemies))
    enemy = Enemy(enemies[rand_enemy])
    turn_order = []
    quantity = random.randrange(1,3)
    # Gets total enemy count and appends it to array
    print(Color.cyan("ROLL INITIATIVE"))
    print("Enemies Rolling...")
    for i in range(quantity):
        total_enemies.append(enemy)
        enemy_inititative = Roll(1,20).total + enemy.speed
        turn_order.append({"entity": {f"{enemy}"}, "roll": enemy_inititative})
    # Initiatives
    print(f"{player['name']} Rolling...")
    player_initiative = Roll(1,20).total + player_stats['speed']
    turn_order.append({'entity': player['name'], 'roll': player_initiative})
    # Sort Turn Order
    sorted_order = sorted(turn_order, key=lambda x: x["roll"], reverse=True)
    # Run Combat
    combat_choice = combat_menu(sorted_order)
    if combat_choice:
        return True
    # If player runs away or loses, exits out of current room
    return False

def combat_menu(sorted_order):
    options = ('Attack', 'Magic', 'Skills', 'Defend', 'Item')
    while True:
        # Menu
        print(sorted_order)
        top_break(Color.red('Combat Menu'))
        print('What would you like to do?')
        for i, option in enumerate(options):
            print(f"{i + 1}. {option}")
        print('0. Run Away')
        # Choice and Check
        choice = int(user_input())
        bottom_break('Combat Menu')
        match choice:
            case 1:
                print("Attack")
                continue
            case 2:
                print("Magic")
                continue
            case 3: 
                print("Skills")
                continue
            case 4:
                print("Defend")
                continue
            # Testing, delete after done
            case 5:
                return True
            case 0:
                print("Run Away")
                return False
            case _:
                print("Please Select an Option!")
                continue