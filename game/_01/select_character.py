from pathlib import Path
from Models.Characters.Player.Player import Player
save_path = Path('game/save')


def select_character():
    while True:
        saves = []
        if not any(save_path.iterdir()):
            print("No saves found.")
            return
        print("\nSelect a Character")
        for save in save_path.iterdir():
            if save.is_file():
                save_file = save.name.replace('.json', '')
                saves.append(save_file)
                print(f"{save_file}")
        character_select = input('')
        if not character_select in saves:
            print("Character not found")
            continue
        print(f"{character_select} loading...")
        data = Player().load_from_file(character_select)
        if not data:
            print(f"Could not load {character_select}")
            continue
        return data
        
