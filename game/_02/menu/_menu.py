import sys
from .view_stats import view_stats

def game_menu(player):
    while True:
        print('=====================================')
        print(f"{player['name']} the {player['class']}")
        print('1. Town\n2. Dungeon\n3. Rest\n4. View Character\n0. Quit')
        choice = input('Where would you like to go?: ')
        match int(choice):
            case 1:
                print('loading town...')
                break
            case 2:
                print('loading dungeon')
                break
            case 3:
                print('resting...')
                break
            case 4:
                view_stats(player)
                break
            case 0:
                end = input('End session?(y to exit): ')
                if end == 'y':
                    print('Exiting\nBye!')
                    sys.exit(0)
                else:
                    continue
            case _:
                print('Option not available...')
                continue
