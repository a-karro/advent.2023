from golden import retriever
_digits = "0,1,2,3,4,5,6,7,8,9,zero,one,two,three,four,five,six,seven,eight,nine"
digits = {i: _digits[::i].split(",")[::i] for i in [-1, 1]}


def find_first_digit(where, direction, part):
    where = where[::direction]
    lim = 10 if part == 1 else 20
    pos = len(where) + 1
    res = -1
    for i, x in enumerate(digits[direction][:lim]):
        if (cur := where.find(x)) != -1:
            if pos > cur:
                pos = cur
                res = i % 10
    return res


p1 = p2 = 0
for n in retriever(2023, 1).read().splitlines():
    p1 += find_first_digit(n, 1, 1) * 10 + find_first_digit(n, -1, 1)
    p2 += find_first_digit(n, 1, 2) * 10 + find_first_digit(n, -1, 2)

print("Puzzle 1.1: ", p1)
print("Puzzle 1.2: ", p2)
