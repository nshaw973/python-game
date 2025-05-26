from game import menu_screen, run_game

def start_game():
    player = menu_screen()
    run_game(player)
    
start_game()