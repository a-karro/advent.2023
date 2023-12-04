from golden import retriever
lines = retriever(2023, 4).read().splitlines()

times = [1] * len(lines)

part1 = 0
for i, line in enumerate(lines):
    card, points = line.split(":")
    numbers, winning = points.split("|")
    numbers = numbers.split()
    winning = winning.split()
    won = len(set(set(numbers) & set(winning)))
    if won > 0:
        part1 += 2**(won - 1)
    for j in range(i + 1, i + won + 1):
        times[j] += times[i]

print("Puzzle 4.1:", part1)
print("Puzzle 4.2:", sum(times))
