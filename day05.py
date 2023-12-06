from golden import retriever


def overlap(r1, r2):
    res = [None] * 3
    if r1[1] < r2[0]:
        return [r1, None, None]
    if r1[0] > r2[1]:
        return [None, None, r1]
    res[1] = max(r1[0], r2[0]), min(r1[-1], r2[-1])
    if r1[0] < r2[0]:
        res[0] = (r1[0], r2[0]-1)
    if r1[1] > r2[1]:
        res[2] = (r2[1] + 1, r1[1])
    return res


def transform2(rng: tuple, map_entry: tuple):
    mappable_range = (map_entry[1], map_entry[1] + map_entry[2] - 1)
    dest_range = (map_entry[0], map_entry[0] + map_entry[2] - 1)
    overlaps = overlap(rng, mappable_range)
    if overlaps[1]:
        mid = list(overlaps[1])
        mid_offset = abs(mid[0] - mappable_range[0])
        overlap_width = abs(mid[1] - mid[0]) + 1
        mid[0] = dest_range[0] + mid_offset
        mid[1] = dest_range[0] + mid_offset + overlap_width - 1
        return tuple(mid)
    return None


def descend(cur, level):
    m = maps[level]
    for lvl in m:
        if lvl[1] <= cur <= lvl[1] + lvl[2]:
            if level + 1 == len(maps):
                return lvl[0] + cur - lvl[1]
            else:
                return descend(lvl[0] + cur - lvl[1], level + 1)
    if level + 1 == len(maps):
        return cur
    else:
        return descend(cur, level + 1)


lines = retriever(2023, 5).read()

mapping = lines.split("\n\n")
seeds = [i for i in map(int, mapping[0].split(":")[1].split())]

maps = []
for map_ in mapping[1:]:
    map_ = map_.split("\n")[1:]
    r = []
    for entry in map_:
        d, s, l = entry.split()
        r.append((int(d), int(s), int(l)))
    maps.append(r)

print("Puzzle 5.1:", min(descend(seed, 0) for seed in seeds))

ranges = [(seeds[i], seeds[i] + seeds[i+1]) for i in range(0, len(seeds), 2)]
for map_ in maps:
    new_ranges = set()
    for range_ in ranges:
        overlaps = []
        for entry_ in map_:
            mappable_range = (entry_[1], entry_[1] + entry_[2] - 1)
            overlaps.append(overlap(range_, mappable_range))
        if all(o[1] is None for o in overlaps):
            new_ranges.add(range_)
        else:
            to_check = set()
            for o in [x[0] for x in overlaps]:
                if o and o != range_:
                    to_check.add(o)
            for o in [x[2] for x in overlaps]:
                if o and o != range_:
                    to_check.add(o)
            for o in [x[1] for x in overlaps if x[1]]:
                for m in map_:
                    if (tx := transform2(o, m)) is not None:
                        new_ranges.add(tx)
            ranges.extend([tc for tc in to_check])
    ranges = list(new_ranges)

print("Puzzle 5.2:", sorted(list(set(x[0] for x in ranges)))[0])
