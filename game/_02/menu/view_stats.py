from core import Color, bottom_break

def view_stats(player):
    print(f"<<<========||{Color.cyan(player['name'])}||========>>>")
    print(f"Class: {Color.get_class_color(player['archetype'])}")
    print(f"Level: {player['level']}")
    print(Color.blue('Stats:'))
    print('----------')
    for key, stat in player['stats'].items():
        print(f"\t{key}: {stat}")
    print(Color.blue('Equipment:'))
    print('----------')
    for key, item in player['equipment'].items():
        print(f"\t{key}: {item}")
    bottom_break(player['name'])