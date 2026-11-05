# Mystery Island - The Lost Lighthouse

## Setup
Python 3.12.3, no external libs
git clone ... / cd mystery-island

## How to run
python3 main.py

## Game rules
- 5 locations: Beach -> Jungle -> Cave -> Old Bridge -> Lighthouse
- Energy starts 5, each legal move costs 1. Invalid input costs 0.
- Inventory: rope in Jungle, lantern in Cave, each once
- Old Bridge requires rope, Lighthouse entry requires lantern, beacon requires lantern at Lighthouse
- Win: light beacon at Lighthouse with energy >0. Lose: energy 0.

## Controls
north/south/east/west, take rope, take lantern, light beacon, look, inventory, quit

## Example win path
north, take rope, north, take lantern, east, east, light beacon

## How to run tests
python3 -m unittest discover -s tests -v

## Known limits
- No save/load
- Case-insensitive but must use direction words, not location names

## Known limits
- No save/load, no secret collectible yet
- Energy never goes negative (clamped at 0)

## What I learned (AI learning log)
1. Topic: input() returns string -> AI said: input always str -> My experiment: typed 5, type was str, int("5")+10=15 -> Conclusion: must convert
2. Topic: if/elif order -> AI said: first True wins -> My experiment: score 85 printed pass not excellent -> Conclusion: check strict condition first

## Concept I understand now that I didn't before is...
Write 3-4 lines yourself — e.g., why return is better than print for testable functions, or why while loop needs a flag