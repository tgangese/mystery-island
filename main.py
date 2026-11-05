from game import new_game, available_actions, apply_action

def main():
    print("="*40)
    print("MYSTERY ISLAND - The Lost Lighthouse")
    print("="*40)
    
    while True:  # replay loop
        name = input("\nWhat is your name? ").strip() or "Explorer"
        player = new_game(name)
        print(f"\nWelcome, {name}! Energy: {player['energy']}\n")

        while not player["game_over"]:
            print(f"--- {player['location']} --- Energy: {player['energy']}")
            print(f"Inventory: {player['inventory'] or 'empty'}")
            print(f"Actions: {', '.join(available_actions(player))}")
            msg = apply_action(player, input("> "))
            print(msg)
            if player["energy"] <= 0 and not player["won"]:
                print("\n*** GAME OVER - You ran out of energy before rescue ***")

        if player["won"]:
            print("\n*** VICTORY! ***")
        else:
            print("\n*** DEFEAT ***")

        again = input("\nPlay again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
