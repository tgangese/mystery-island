# game.py - game logic, testable without input()
def new_game(name):
    """Create fresh player state. Recommended from spec."""
    return {
        "name": name,
        "location": "Beach",
        "energy": 5,
        "inventory": [],
        "game_over": False,
        "won": False
    }

# Map: which locations connect to which
LOCATIONS = {
    "Beach": {"description": "Sandy beach, jungle to north", "north": "Jungle"},
    "Jungle": {"description": "Thick jungle, cave to north, beach to south", "south": "Beach", "north": "Cave"},
    "Cave": {"description": "Dark cave, bridge to east", "south": "Jungle", "east": "Old Bridge"},
    "Old Bridge": {"description": "Rickety bridge to lighthouse", "west": "Cave", "east": "Lighthouse"},
    "Lighthouse": {"description": "The dark lighthouse!", "west": "Old Bridge"}
}

def available_actions(player):
    """Return list of actions player can take now."""
    loc = player["location"]
    actions = ["look", "inventory", "quit"]
    # add movement actions from LOCATIONS[loc] keys that are directions
    for direction in ["north", "south", "east", "west"]:
        if direction in LOCATIONS[loc]:
            actions.append(direction)
    return actions

def apply_action(player, action):
    """Change player state, return message. Does NOT do input()."""
    action = action.strip().lower()
    
    if action == "quit":
        player["game_over"] = True
        return "You quit."
    
    if action in ["north", "south", "east", "west"]:
        current = player["location"]
        if action in LOCATIONS[current]:
            # TODO: Should this cost energy? Spec says legal move costs 1
            # Check energy first
            if player["energy"] <= 0:
                player["game_over"] = True
                return "Out of energy! You collapse."
            
            new_loc = LOCATIONS[current][action]
            player["location"] = new_loc
            player["energy"] -= 1  # TODO: what if energy becomes 0 after move?
            if player["energy"] <= 0:
                player["game_over"] = True
                return f"You moved to {new_loc} but ran out of energy!"
            return f"You moved to {new_loc}. Energy: {player['energy']}"
        else:
            # TODO: Wrong-direction move should be rejected WITHOUT cost
            return f"Cannot go {action} from {current}."
    
    if action == "look":
        return LOCATIONS[player["location"]]["description"]
    
    if action == "inventory":
        inv = player["inventory"]
        return f"Inventory: {inv if inv else 'empty'}, Energy: {player['energy']}"
    
    return f"Invalid action '{action}'"