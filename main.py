from game import menu_screen, run_game

def start_game():
    # Get player
    player = menu_screen()
    # Once player is chosen, run the game loop
    run_game(player)
# Initialize game
start_game()