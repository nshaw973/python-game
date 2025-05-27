from .menu._menu import game_menu
from core import Color
def run_game(player):
    print(f"{player['name']} the {Color.get_class_color(player['archetype'])} is ready for adventure!")
    while True:
        game_menu(player)