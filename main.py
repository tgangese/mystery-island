# main.py - now uses game.py
from game import new_game, available_actions, apply_action

def main():
    # ... your title code ...
    name = input("Name: ").strip() or "Explorer"
    player = new_game(name)
    
    while not player["game_over"]:
        print(f"\n--- {player['location']} --- Energy: {player['energy']}")
        print(f"Actions: {', '.join(available_actions(player))} (type north/south/east/west)")
        choice = input("> ")
        msg = apply_action(player, choice)
        print(msg)
        
        # check loss
        if player["energy"] <= 0 and not player["won"]:
            print("GAME OVER - you ran out of energy!")
            break
    
    print(f"Goodbye, {player['name']}!")

if __name__ == "__main__":
    main()