import itertools
from golden import retriever

lines = retriever(2023, 11).read().splitlines()


def solve(part1):
    mul = 2 if part1 else 1000000
    M1 = []
    rows = []
    cols = []
    galaxies = []
    for y, line in enumerate(lines):
        r = []
        for x, e in enumerate(line):
            r.append(e)
            if e == "#":
                galaxies.append((x, y))
        M1.append(r)
        if len(set(r)) == 1:
            rows.append(y)
    for x in range(len(M1[1])):
        col = []
        for y in range(len(M1)):
            col.append(M1[y][x])
        if len(set(col)) == 1:
            cols.append(x)

    for y in rows:
        for i, g in enumerate(galaxies):
            if g[1] > y:
                galaxies[i] = (g[0], g[1] + mul - 1)
        for i, c in enumerate(rows):
            if c > y:
                rows[i] = rows[i] + mul - 1

    for x in cols:
        for i, g in enumerate(galaxies):
            if g[0] > x:
                galaxies[i] = (g[0] + mul - 1, g[1])
        for i, c in enumerate(cols):
            if c > x:
                cols[i] = cols[i] + mul - 1

    combos = list(itertools.combinations(galaxies, 2))
    resp = 0
    for combo in combos:
        resp += abs(combo[0][0] - combo[1][0]) + abs(combo[0][1] - combo[1][1])

    return resp


print("Puzzle 11.1:", solve(part1=True))
print("Puzzle 11.2:", solve(part1=False))
