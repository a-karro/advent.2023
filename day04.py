from golden import retriever
lines = retriever(2023, 4).read().splitlines()

times = [1] * len(lines)

part1 = 0
for i, line in enumerate(lines):
    card, points = line.split(":")
    numbers, winning = points.split("|")
    numbers = numbers.split()
    winning = winning.split()
    cnt = cnt2 = 0
    for nmb in numbers:
        if nmb in winning:
            cnt2 += 1
            if cnt == 0:
                cnt = 1
            else:
                cnt *= 2
    part1 += cnt
    for j in range(i + 1, i + cnt2 + 1):
        times[j] += times[i]

print("Puzzle 4.1:", part1)
print("Puzzle 4.2:", sum(times))
