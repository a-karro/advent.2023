from golden import retriever
import functools

lines = retriever(2023, 7).read().splitlines()


def poker(h):
    h = [c for c in h]
    if len(set(h)) == 1:
        return 7   # five of a kind
    if (len(t := set(h))) == 2:
        t = list(t)
        if h.count(t[0]) == 4 or h.count(t[1]) == 4:
            return 6  # four of a kind
        else:
            return 5  # full house
    if len(t := set(h)) == 3:
        if any(h.count(c) == 3 for c in t):
            return 3  # three of a kind
        else:
            return 2  # two pair
    if len(set(h)) == 4:
        return 1  # one pair
    if len(set(h)) == 5:
        return 0  # high card


def max_hand(hands_list):
    r = hands_list[0]
    for h in hands_list[1:]:
        if compare(h, r) == 1:
            r = h
    return r


def compare(hand1, hand2):
    rlocal = "23456789TJQKA"
    h1 = poker(hand1)
    h2 = poker(hand2)
    if h1 > h2:
        return 1
    elif h1 < h2:
        return -1
    else:
        for i, h1 in enumerate(hand1):
            if rlocal.index(h1) > rlocal.index(hand2[i]):
                return 1
            elif rlocal.index(h1) < rlocal.index(hand2[i]):
                return -1
    return 0


def compare_regular(hand1, hand2):
    return compare(hand1[0], hand2[0])


def compare_jokerized(hand1, hand2):
    rlocal = "J23456789TQKA"
    h1 = hand1[1]
    h2 = hand2[1]
    h1 = poker(h1)
    h2 = poker(h2)
    if h1 > h2:
        return 1
    elif h1 < h2:
        return -1
    else:
        hand1 = hand1[0]
        hand2 = hand2[0]
        for i in range(len(hand1)):
            if rlocal.index(hand1[i]) > rlocal.index(hand2[i]):
                return 1
            elif rlocal.index(hand1[i]) < rlocal.index(hand2[i]):
                return -1
    return 0


def jokerize(hand):
    if (idx := hand.find('J')) == -1:
        return [hand]
    else:
        res = []
        for r in "23456789TQKA":
            s = hand[:idx] + r + hand[idx+1:]
            res.extend(jokerize(s))
        return res


hands = []

for line in lines:
    hand, bid = line.split()
    bid = int(bid)
    hands.append((hand, max_hand(jokerize(hand)), bid))


p1 = []
for i, hand in enumerate(sorted(hands, key=functools.cmp_to_key(compare_regular))):
    p1.append((i+1) * hand[2])
print("Puzzle 7.1:", sum(p1))

p2 = []
for i, hand in enumerate(sorted(hands, key=functools.cmp_to_key(compare_jokerized))):
    p2.append((i+1) * hand[2])

print("Puzzle 7.1:", sum(p2))
