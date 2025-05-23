from .create_character import create_character
from .select_character import select_character
from pathlib import Path
save_path = Path('game/save')
def menu_screen():
    while True:
        option = input(f"Choose an option (1-3):\n1. New Game\n2. Continue\n3. Quit\n")

        # Creates Save Directory if it doesn't exist
        save_path.mkdir(parents=True, exist_ok=True)

        # Runs Function based on user input
        match option:
            case '1':
                # Creates New Character
                player = create_character()
                return player
            case '2':
                # Iterates through save files, if none are found then returns to menu
                player = select_character()
                return player
            case '3':
                #Exits Game
                print("Exiting...")
                return
            case _:
                # Catches any incorrect input
                print("Option not found")
                continue
        