
# score=85
# if score>50: print('pass')
# elif score>80: print('excellent')
# else: print('fail')

# inventory=['rope']
# if 'rope' in inventory and 'lantern' in inventory: print('can win')
# elif 'rope' in inventory or 'lantern' in inventory: print('almost ready')
# else: print('need items')

# Drill 1 - weather
temp = int(input("Temperature? "))
raining_input = input("Raining? yes/no: ").strip().lower()
raining = raining_input == "yes"

if temp > 15 and not raining:
    print("safe")
else:
    print("not safe")

# Drill 2 - bridge (test with 3 different inventories)
inventory = ["rope"]  # change to [] and ["rope","lantern"] and run 3 times
if "rope" in inventory:
    print("You can cross the bridge")
else:
    print("You need rope to cross Old Bridge")

# Drill 3 - menu - THE KEY PATTERN FOR CHECKPOINT A
choice = input("1: Beach, 2: Jungle, q: quit > ").strip().lower()
if choice == "1":
    print("Going to Beach")
elif choice == "2":
    print("Going to Jungle")
elif choice == "q":
    print("Quitting")
else:
    print(f"Invalid choice '{choice}' - try 1, 2, or q")