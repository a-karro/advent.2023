from golden import retriever
from collections import deque


lines = retriever(2023, 9).read().splitlines()

p1 = p2 = 0

for line in lines:
    NH = [deque([i for i in map(int, line.split())])]
    while set(NH[-1]) != {0}:
        R = deque()
        for i in range(len(NH[-1]) - 1):
            R.append(NH[-1][i + 1] - NH[-1][i])
        NH.append(R)
    for nh in NH:
        nh.append(0)
        nh.appendleft(0)
    for i in range(len(NH) - 1, 0, -1):
        NH[i - 1][-1] = NH[i][-1] + NH[i-1][-2]
        NH[i - 1][0] = NH[i - 1][1] - NH[i][0]
    p1 += NH[0][-1]
    p2 += NH[0][0]

print("Puzzle 9.1:", p1)
print("Puzzle 9.2:", p2)
