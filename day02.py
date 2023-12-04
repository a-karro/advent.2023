from collections import defaultdict
from math import prod
from golden import retriever

possibles = powers = 0
max_c = {"red": 12, "green": 13, "blue": 14}

for line in retriever(2023, 2).read().splitlines():
    possible = True
    power = defaultdict(int)
    game_id, game_data = line.split(": ")
    for entry in game_data.split(";"):
        cubes = entry.split(",")
        for c in cubes:
            cnt, col = c.split()
            cnt = int(cnt)
            possible = possible and max_c[col] >= cnt
            power[col] = max(power[col], cnt)
    powers += prod(power.values())
    if possible:
        possibles += int(game_id.split()[1])

print("Puzzle 2,1:", possibles)
print("Puzzle 2.2:", powers)
