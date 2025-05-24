# Libraries and more
from pathlib import Path
# Models
from core import user_input, exit_game, Color
# Utils
from .create_character import create_character
from .select_character import select_character


save_path = Path('game/save')
def menu_screen():
    # Creates Save Directory if it doesn't exist
    save_path.mkdir(parents=True, exist_ok=True)
    while True:
        print('<<<=======||GAME||========>>>')
        print(f"{Color.magenta('MAIN MENU')}")
        print(f"Choose an option (1-3):\n{Color.green('1. New Game')}\n{Color.yellow('2. Continue')}\n{Color.red('0. Quit')}")
        option = user_input()
        print('<<<=======||====||========>>>')
        # Runs Function based on user input
        match int(option):
            case 1:
                # Creates New Character
                player = create_character()
                if player:
                    return player
                else:
                    continue
            case 2:
                # Iterates through save files, if none are found then returns to menu
                player = select_character()
                if player:
                    return player
                else:
                    continue
            case 0:
                exit_game()
                continue
            case _:
                # Catches any incorrect input
                print("Option not found")
                continue
        