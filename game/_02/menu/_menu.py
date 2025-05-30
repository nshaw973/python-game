from .view_stats import view_stats
from .view_dungeons import view_dungeons
from game.maps.load_map import load_map
from core import user_input, exit_game, bottom_break, top_break, Color

def game_menu(player):
    while True:
        location = 'GAME MENU'
        top_break(Color.cyan(location))
        print(f"{player['name']} the {Color.get_class_color(player['archetype'])}")
        print('1. Town\n2. Dungeon\n3. Rest\n4. View Character\n0. Quit')
        print('Where would you like to go?:')
        choice = user_input()
        bottom_break(location)
        match choice:
            case '1':
                print('loading town...')
                break
            case '2':
                dungeon = view_dungeons(player)
                load_map(player, dungeon)
                break
            case '3':
                print('resting...')
                break
            case '4':
                view_stats(player)
                break
            case '0':
                exit_game()
                continue
            case _:
                print('Option not available...')
                continue
