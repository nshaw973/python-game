from core import Color, user_input

def view_dungeons(player):
    dungeons = player['dungeons']
    while True:
        print("Select a location:")
        for i, dungeon in dungeons:
            print(f"{i}. {dungeon}")
        print("0. Go Back")
        choice = int(user_input())
        if choice > len(dungeons):
            print(Color.red("Option not available!"))
        elif choice == 0:
            return
        return dungeons[choice]
