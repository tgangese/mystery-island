# game.py - game logic, testable without input()
def new_game(name):
    return {
        "name": name,
        "location": "Beach",
        "energy": 5,
        "inventory": [],
        "game_over": False,
        "won": False
    }

ITEMS = {
    "Beach": None,
    "Jungle": "rope",
    "Cave": "lantern",
    "Old Bridge": None,
    "Lighthouse": None
}

LOCATIONS = {
    "Beach": {"description": "Sandy beach, jungle to north", "north": "Jungle"},
    "Jungle": {"description": "Thick jungle, cave to north, beach to south", "south": "Beach", "north": "Cave"},
    "Cave": {"description": "Dark cave, bridge to east", "south": "Jungle", "east": "Old Bridge"},
    "Old Bridge": {"description": "Rickety bridge to lighthouse", "west": "Cave", "east": "Lighthouse"},
    "Lighthouse": {"description": "The dark lighthouse!", "west": "Old Bridge"}
}

def available_actions(player):
    loc = player["location"]
    actions = ["look", "inventory", "quit"]
    item_here = ITEMS.get(loc)
    if item_here and item_here not in player["inventory"]:
        actions.append(f"take {item_here}")
    for direction in ["north", "south", "east", "west"]:
        if direction in LOCATIONS[loc]:
            actions.append(direction)
    return actions

def apply_action(player, action):
    action = action.strip().lower()
    
    if action == "quit":
        player["game_over"] = True
        return "You quit."
    
    if action.startswith("take "):
        wanted = action[5:].strip()
        item_here = ITEMS.get(player["location"])
        if item_here == wanted and wanted not in player["inventory"]:
            player["inventory"].append(wanted)
            return f"You picked up {wanted}!"
        elif wanted in player["inventory"]:
            return f"You already have {wanted}."
        else:
            return f"No {wanted} here."
    
    if action == "look":
        return LOCATIONS[player["location"]]["description"]
    
    if action == "inventory":
        inv = player["inventory"]
        return f"Inventory: {inv if inv else 'empty'}, Energy: {player['energy']}"
    
    # Movement - only after all other commands
    if action in ["north", "south", "east", "west"]:
        current = player["location"]
        if action not in LOCATIONS[current]:
            return f"Cannot go {action} from {current}."
        
        dest = LOCATIONS[current][action]

        # BLOCKS - T6 and T7
        if current == "Cave" and dest == "Old Bridge":
            if "rope" not in player["inventory"]:
                return "The bridge is broken. You need rope to cross."
        if current == "Old Bridge" and dest == "Lighthouse":
            if "lantern" not in player["inventory"]:
                return "It's too dark to enter Lighthouse. You need lantern."

        if player["energy"] <= 0:
            player["game_over"] = True
            return "Out of energy! You collapse."

        player["location"] = dest
        player["energy"] -= 1
        if player["energy"] <= 0:
            player["game_over"] = True
            return f"You moved to {dest} but ran out of energy!"
        return f"You moved to {dest}. Energy: {player['energy']}"
    
    return f"Invalid action '{action}'"