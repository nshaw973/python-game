from core import Color, user_input
from .submenus import attack_menu, magic_menu, item_menu
def combat_menu(player):
    options = ('Attack', 'Magic', 'Defend', 'Item', 'Run')
    print("Select combat option")
    for i, option in options:
        print(f"{i}. {option}")
    while True:
        choice = user_input
        match choice:
            # Attack Menu
            case '1':
                attack_menu(player)
                break
            # Magic Menu
            case '2':
                magic_menu(player)
                break
            # Defend
            case '3':
                item_menu(player)
                break
            # Item
            case '4':
                break
            # Run
            case '5':
                print("escaped dungeon!")
                return
            case _:
                print(Color.red("Input not accepted."))
                continue