from game._01._01menu import menu_screen
from game._02.run_game import run_game

def start_game():
    player = menu_screen()
    run_game(player)
start_game()