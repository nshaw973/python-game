from pathlib import Path
from Models import Player
from core import user_input, Color
save_path = Path('game/save')


def select_character():
    while True:
        # Check for saves
        saves = []
        for save in save_path.glob('*.json'):
            save_name = save.stem
            saves.append(save_name)
        if not saves:
            print('No characters found!')
            return None
        
        # Options for Saves
        print("Select a Character:")
        for i, save in enumerate(saves, 1):
            print(f"{i}. {Color.random(save)}")
        print("0. Back to Menu")

        # Get user input
        try:
            print('Enter a number (0 to cancel):')
            choice = user_input()

            if choice == '0':
                return None
            selected_index = int(choice) - 1

            if 0 <= selected_index < len(saves):
                selected_char = saves[selected_index]
                print(f"Loading {selected_char}...")

                # Load Character
                data = Player.load_from_file(selected_char)
                if data:
                    return data
                else:
                    print(f"Failed to load {selected_char}")
            else:
                print('Invalid Selection!')
        except ValueError:
            print('Please enter a valid number!')
        
