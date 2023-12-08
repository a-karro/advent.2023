from math import gcd
from copy import deepcopy
from golden import retriever


lines = retriever(2023, 8).read().strip()

instr, moves = lines.split("\n\n")
MAP = {}

for j in moves.split("\n"):
    n, v = j.split(" = ")
    l, r = v.split(", ")
    l = l[1:]
    r = r[:-1]
    MAP[n] = (l, r)

instr = [i for i in map(int, instr.replace("R", "1").replace("L", "0"))]
LI = len(instr)

cnt = 0
cur = "AAA"
while True:
    if MAP[cur][instr[cnt % LI]] == "ZZZ":
        break
    cur = MAP[cur][instr[cnt % LI]]
    cnt += 1

print("Puzzle 6.1:", cnt + 1)

cnt = 0
cur = [k for k in MAP.keys() if k[-1] == "A"]

beg = deepcopy(cur)
loops = {k: [] for k in cur}

while set(cur) != {"="}:
    for i in range(len(cur)):
        if cur[i] == "=":
            continue
        cur[i] = MAP[cur[i]][instr[cnt % LI]]
        if cur[i][-1] == "Z":
            loops[beg[i]].append(cnt)
            if len(loops[beg[i]]) == 2:
                cur[i] = "="
    cnt += 1

c = [i[1] - i[0] for i in loops.values()]

# math in Python 3.8 doesn't have lcm, so
lcm = 1
for i in c:
    lcm = lcm * i // gcd(lcm, i)

print("Puzzle 6.2:", lcm)
