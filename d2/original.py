import math
# 1. parse and ds
games = {}
for line in open("d2/input.txt").read().splitlines():
    g, p = line.split(": ")
    _id = int(g.split(" ")[1])

    games[_id] = []
    for r in p.split(";"):
        cur = {}
        for t in r.strip().split(", "):
            c, col = t.split(" ")
            cur[col] = int(c)
        games[_id].append(cur)

total = {'red': 12, 'green': 13, 'blue': 14}
p1, p2 = 0, 0
# 2. algo
for gid, rounds in games.items():
    skip = False
    max_cols = {key: 0 for key in total}
    for r in rounds:
        for col, count in r.items():
            if max_cols[col] < count:
                max_cols[col] = count
            if count > total[col]:
                skip = True
    if not skip:
        p1 += gid
    p2 += math.prod(max_cols.values())

print(f"p1: {p1}, p2: {p2}")