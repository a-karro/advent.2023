from golden import retriever
from math import prod

lines = [i.split(":")[1] for i in retriever(2023, 6).read().splitlines()]

times = [i for i in map(int, lines[0].split())]
records = [i for i in map(int, lines[1].split())]

p1 = []
for i in range(len(records)):
    rec = records[i]
    time = times[i]
    p1.append(sum(1 for j in range(time) if j * (time - j) > rec))
print("Puzzle 6.1:", prod(p1))

time = int(lines[0].replace(" ", ""))
record = int(lines[1].replace(" ", ""))

rb = 0
while rb * (time - rb) < record:
    rb += 1

re = time
while re * (time - re) < record:
    re -= 1

print("Puzzle 6.2:", re - rb + 1)
