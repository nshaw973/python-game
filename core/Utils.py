import sys
from .Color import Color

def user_input():
    user_input = input(Color.blue('>>> ')).strip()
    return user_input

def exit_game():
    print('Would you like to exit the game? (y to exit):')
    choice = user_input()
    if choice == 'y':
        print('Exiting\nBye!')
        sys.exit(0)
    else:
        return