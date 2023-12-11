import itertools
_inp = [list(r) for r in open("d11/input.txt").read().splitlines()]

exp_x, exp_y, galaxies = [], [], []
for y in range(len(_inp)):
    if all([el == '.' for el in _inp[y]]):
        exp_y.append(y)

for x in range(len(_inp[0])):
    if all([_inp[y][x] == '.' for y in range(len(_inp))]):
        exp_x.append(x)

for y in range(len(_inp)):
    for x in range(len(_inp[0])):
        if _inp[y][x] == '#':
            galaxies.append((x, y))

def shortest(t=False, _sum=0):
    for p1, p2 in itertools.combinations(galaxies, 2):
        dist, x_range, y_range = 0, range(min(p1[0], p2[0]), max(p1[0], p2[0])),\
            range(min(p1[1], p2[1]), max(p1[1], p2[1]))
        dist += len([x for x in x_range if x not in exp_x])
        dist += len([y for y in y_range if y not in exp_y])
        expansion = len([p for p in exp_x if p in x_range]) + len([p for p in exp_y if p in y_range])
        _sum += expansion * (1000000 if t else 2) + dist
    return _sum

print(shortest(), shortest(t=True))





