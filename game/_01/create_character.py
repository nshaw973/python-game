from pathlib import Path
from Models.Characters.Player.Player import Player
save_path = Path('game/save')

def create_character():
    new_character = Player()
    new_character.save_to_file()
    player = Player.load_from_file(new_character.name)
    if player:
        return player
    else:
        print('Failed failed to load character')