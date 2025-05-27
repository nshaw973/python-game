from .view_stats import view_stats
from core import user_input, exit_game, bottom_break, top_break, Color, Roll

def game_menu(player):
    while True:
        location = 'GAME MENU'
        top_break(Color.cyan(location))
        print(f"{player['name']} the {Color.get_class_color(player['class'])} lvl: {Color.get_class_color(player['level'])}")
        print('1. Town\n2. Dungeon\n3. Rest\n4. View Character\n0. Quit')
        print('Where would you like to go?:')
        choice = user_input()
        bottom_break(location)
        match choice:
            case '1':
                print('loading town...')
                break
            case '2':
                print('loading dungeon')
                break
            case '3':
                print('resting...')
                break
            case '4':
                view_stats(player)
                break
            case '5':
                print("Rolling Dice")
                while True:
                    print("How many sides? 4 - 20 even:")
                    sides = int(user_input())
                    if 4 > sides > 20:
                        print("Mustbe between 4 - 20 or more sides")
                        continue
                    elif sides % 2 != 0:
                        print("Must be even!")
                        continue
                    else:
                        break
                while True:    
                    print("How many dice?(10 MAX):")
                    quantity = int(user_input())
                    if quantity > 10:
                        print("Cannot be more than 10!")
                    result = Roll(quantity, sides)
                    return result
            case '0':
                exit_game()
                continue
            case _:
                print('Option not available...')
                continue
