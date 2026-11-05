# Mystery Island - The Lost Lighthouse
Player wakes on beach after storm. Lighthouse dark, bridge locked, rescue boat needs beacon.

## Setup
Python 3.12.3, standard library only
No external dependencies

## How to run
python3 main.py

## Game rules
- 5 locations: Beach -> Jungle -> Cave -> Old Bridge -> Lighthouse
- Energy starts at 5, each legal move costs 1. Invalid input costs 0. Energy never goes negative.
- Inventory: rope in Jungle, lantern in Cave, each can be taken once
- Old Bridge requires rope, Lighthouse entry requires lantern
- Beacon requires lantern at Lighthouse
- Win: light beacon at Lighthouse with energy >0
- Lose: energy reaches 0

## Controls
north / south / east / west, take rope, take lantern, light beacon, look, inventory, quit
All inputs are case-insensitive and trimmed: `  Q  ` works as `q`

## Example win path (7 commands, wins with 1 energy left)
north
take rope
north
take lantern
east
east
light beacon

## Example losing path
Keep moving north/south until energy 0

## How to run tests
python3 -m unittest discover -s tests -v
Expected: 10 tests OK (T1-T10)

## Known limits
- No save/load
- No secret collectible yet
- Must use direction words, not location names

## What I learned (AI learning log)
1. Topic: input() returns string -> AI said: input always returns str -> My experiment: typed 5, type was str, int("5")+10=15 -> Conclusion: must convert with int()
2. Topic: if/elif order -> AI said: first True wins -> My experiment: score 85 printed "pass" not "excellent" -> Conclusion: check strict condition (>80) before loose (>50)

## Concept I understand now that I didn't before is...
That return gives data to code while print gives data to humans. My apply_action returns a string so tests can check it, and main.py decides to print it. Also that input() always gives a string, so I must use .strip().lower() to make Q and q the same, and that invalid input must never cost energy, otherwise the game becomes unfair and untestable.