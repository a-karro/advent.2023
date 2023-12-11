from golden import retriever


def get_next(curr, D, map_, direct="R"):
    n_x, n_y = curr[0] + dirs[D][0], curr[1] + dirs[D][1]
    e = map_[n_y][n_x]
    k = rights if direct == "R" else lefts
    return next_dir.get((D, e), None), k.get((D, e), None)


next_dir = {
    # (current direction, current pipe) : next direction
    ("N", "|"): "N",
    ("N", "7"): "W",
    ("N", "F"): "E",

    ("E", "J"): "N",
    ("E", "7"): "S",
    ("E", "-"): "E",

    ("W", "-"): "W",
    ("W", "F"): "S",
    ("W", "L"): "N",

    ("S", "|"): "S",
    ("S", "L"): "E",
    ("S", "J"): "W",
}

rights = {
    # (current direction, current pipe) : Current element(s) on the right
    # Note, that we have 3 elements
    #   when facing N and turning left: right, right-top and top
    ("N", "|"): ["E"],
    ("N", "7"): ["E", "NE", "N"],
    ("N", "F"): ["E"],

    ("E", "J"): ["S", "SE", "E"],
    ("E", "7"): ["S"],
    ("E", "-"): ["S"],

    ("W", "-"): ["N"],
    ("W", "F"): ["N", "NW", "W"],
    ("W", "L"): ["N"],

    ("S", "|"): ["W"],
    ("S", "L"): ["W", "SW", "S"],
    ("S", "J"): ["W"],
}

lefts = {
    # (current direction, current pipe) : Current element(s) on the left
    # Note, that we have 3 elements
    #   when facing N and turning right: left, left-top and top
    ("N", "|"): ["W"],
    ("N", "7"): ["W"],
    ("N", "F"): ["N", "NW", "W"],

    ("E", "J"): ["N"],
    ("E", "7"): ["N", "NE", "E"],
    ("E", "-"): ["N"],

    ("W", "-"): ["S"],
    ("W", "F"): ["S"],
    ("W", "L"): ["S", "SW", "W"],

    ("S", "|"): ["E"],
    ("S", "L"): ["E"],
    ("S", "J"): ["E", "SE", "S"],
}

dirs = {
    "N": (0, -1),
    "E": (1, 0),
    "S": (0, 1),
    "W": (-1, 0)
}

dirs_f = {
    "N": (0, -1),
    "NE": (1, -1),
    "NW": (-1, -1),
    "E": (1, 0),
    "SE": (1, 1),
    "S": (0, 1),
    "SW": (-1, 1),
    "W": (-1, 0)
}

turns = {
    # (current direction, next direction) : L or R turn
    ("E", "S"): "R",
    ("S", "W"): "R",
    ("W", "N"): "R",
    ("N", "E"): "R",

    ("E", "N"): "L",
    ("N", "W"): "L",
    ("W", "S"): "L",
    ("S", "E"): "L",
}

potentials = {
    "NS": "|",
    "EW": "-",
    "SW": "7",
    "ES": "F",
    "EN": "L",
    "NW": "J",
}

lines = retriever(2023, 10).read().splitlines()
pipes = []

start = (0, 0)
for y, line in enumerate(lines):
    pipes.append([x for x in line])
    if "S" in line:
        start = (line.index("S"), y)

cur_pos = start
cur_dir = []

for n in dirs:
    nx, ny = start[0] + dirs[n][0], start[1] + dirs[n][1]
    aa = pipes[ny][nx]
    if next_dir.get((n, aa), None):
        cur_dir.append(n)

cd = "".join(sorted(cur_dir))
cur_dir = cd[0]
pipes[start[1]][start[0]] = potentials[cd]

length = 0
path = [cur_pos]
turn_cnt = ""

while True:
    length += 1
    nxt, _ = get_next(cur_pos, cur_dir, pipes)
    nx, ny = cur_pos[0] + dirs[cur_dir][0], cur_pos[1] + dirs[cur_dir][1]
    if (nx, ny) == start:
        break
    cur_pos = nx, ny
    path.append(cur_pos)
    turn_cnt += turns.get((cur_dir, nxt), "")
    cur_dir = nxt

clean_map = [['.'] * len(pipes[0]) for _ in range(len(pipes))]

for p in path:
    x, y = p
    clean_map[y][x] = pipes[y][x]

direction = "R" if turn_cnt.count("R") > turn_cnt.count("L") else "L"
cur_pos = start
cur_dir = cd[0]
while True:
    nxt, inners = get_next(cur_pos, cur_dir, clean_map, direction)
    nx, ny = cur_pos[0] + dirs[cur_dir][0], cur_pos[1] + dirs[cur_dir][1]
    if (nx, ny) == start:
        break
    for p in inners:
        M = dirs_f[p]
        px, py = cur_pos[0] + M[0], cur_pos[1] + M[1]
        if 0 <= px < len(clean_map[0]) and 0 <= py < len(clean_map):
            if clean_map[py][px] == ".":
                clean_map[py][px] = "@"
    cur_pos = nx, ny
    cur_dir = nxt

res = 0
for ln in clean_map:
    s = "".join(ln)
    while s.find("@.") > -1:
        s = s.replace("@.", "@@")
    res += s.count("@")

print("Puzzle 10.1:", length // 2)
print("Puzzle 10.2:", res)
