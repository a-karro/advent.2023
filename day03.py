from collections import defaultdict
from string import digits
from math import prod
from golden import retriever


def neighbors(point, width, height, diagonals=True):
    deltas = [(0, -1), (-1, 0), (0, 1), (1, 0)]
    if diagonals:
        deltas.extend([(-1, -1), (-1, 1), (1, 1), (1, -1)])
    res = []
    for delta in deltas:
        dx, dy = map(lambda a, b: a + b, point, delta)
        if 0 <= dx < width and 0 <= dy < height:
            res.append((dx, dy))
    return res


lines = retriever(2023, 3).read().splitlines()

valid = digits + "."

grid = [[j for j in i] for i in lines]
w = len(grid[0])
h = len(grid)
parts = []

gears = defaultdict(list)

for y in range(h):
    in_prog = False
    is_part = False
    number = ""
    cur_gears = set()
    for x in range(w):
        if grid[y][x] in digits:
            number += grid[y][x]
            if not in_prog:
                in_prog = True
            for xx, yy in neighbors((x, y), w, h):
                is_part = is_part or grid[yy][xx] not in valid
                if grid[yy][xx] == "*":
                    cur_gears.add((xx, yy))
        else:
            if in_prog:
                in_prog = False
                if is_part:
                    parts.append(int(number))
                for g in cur_gears:
                    gears[g].append(int(number))
                number = ""
                is_part = False
                cur_gears = set()
    if in_prog:
        if is_part:
            parts.append(int(number))
    for g in cur_gears:
        gears[g].append(int(number))

print("Puzzle 3.1:", sum(parts))
print("Puzzle 3.2:", sum(prod(gear) for gear in gears.values() if len(gear) == 2))
