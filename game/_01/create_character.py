from pathlib import Path
from Models.Characters.Player.Player import Player
save_path = Path('game/save')

def create_character():
    new_character = Player()
    new_character.save_to_file(new_character.name)
    player = new_character.load_from_file(new_character.name)

    print(f"{new_character.name} has been created!")
    return player