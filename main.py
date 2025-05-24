import sys
from game import menu_screen, run_game

def start_game():
    sys.dont_write_bytecode = True
    player = menu_screen()
    run_game(player)
start_game()