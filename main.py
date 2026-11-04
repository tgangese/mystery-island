# Drill 1 - correct variable + f-string
nickname = input("Nickname: ")
score = 0
print(f"Welcome, {nickname}! Your score is {score}.")
print(f"type(nickname) is {type(nickname)}, type(score) is {type(score)}")

# Drill 2 - the input trap
fav = input("Favorite number? ")  # type 7
print(f"You typed: {fav}, type is {type(fav)}")
fav_number = int(fav)  # convert
print(f"As int + 10 = {fav_number + 10}, type is {type(fav_number)}")

# Drill 3 - future player state
energy = 5
location = "Beach"
has_lantern = False
print(f"Energy: {energy}, Location: {location}, Has lantern: {has_lantern}")
print(type(energy), type(location), type(has_lantern))