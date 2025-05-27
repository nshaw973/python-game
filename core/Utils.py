import sys
from .Color import Color

def user_input():
    # User should only be inputing numbers
    while True:
        user_input = input(Color.blue('>>> ')).strip().lower()
        return user_input

def exit_game():
    print('Would you like to exit the game? (y to exit):')
    choice = user_input()
    if choice == 'y':
        print('Exiting\nBye!')
        sys.exit(0)
    else:
        return

def top_break(str):
    print(f'<<<========||{str}||========>>>')

def bottom_break(title: str):
    length = 0
    if title:
        length = len(title)
    print(f'<<<========||{str("=" * length)}||========>>>')
 