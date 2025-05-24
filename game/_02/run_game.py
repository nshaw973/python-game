from .menu._menu import game_menu
def run_game(player):
    print(f"{player['name']} the {player['class']} is ready for adventure!")
    while True:
        game_menu(player)