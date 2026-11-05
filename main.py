# main.py - Checkpoint A
def display_title():
    print("="*40)
    print("MYSTERY ISLAND - The Lost Lighthouse")
    print("="*40)
    print("You wake up on a beach. The lighthouse is dark.")
    print("Restore the beacon before rescue boat arrives.")
    print()

def main():
    display_title()
    name = input("What is your name, explorer? ").strip()
    if not name:
        name = "Explorer"
    print(f"\nWelcome, {name}!\n")
    
    # This is the loop that repeats the menu - ANSWER THIS LATER
    game_running = True
    while game_running:
        print("--- Beach ---")
        print("Waves crash. You see jungle inland.")
        print("\nWhat do you do?")
        print("1. Look around")
        print("2. Go to Jungle (not built yet)")
        print("q. Quit")
        
        choice = input("> ").strip().lower()  # <-- Why strip().lower()?
        
        # TODO: Fill these branches
        if choice == "1":
            print("You find footprints leading to the jungle.\n")
        elif choice == "2":
            print("Jungle path is blocked for now (Checkpoint B).\n")
        elif choice == "q" or choice == "quit":
            print(f"Goodbye, {name}!")
            game_running = False
        else:
            # TODO: What should happen here? Should game_running change?
            print(f"'{choice}' is not valid. Try 1, 2, or q.\n")
            # Should this consume energy? No, per spec.

if __name__ == "__main__":
    main()