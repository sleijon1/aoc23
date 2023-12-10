_inp = open("d10/input.txt").read().splitlines()
_inp = [list(string) for string in _inp]
_inp = [list(';'.join(r)) for r in _inp]
x_arr = [list(';'*len(_inp[0])) for _ in _inp]
new_inp = []
for i in range(len(_inp)):
    new_inp.append(_inp[i])
    new_inp.append(x_arr[i])
_inp = new_inp


s = None
c = '|-JL7F'
for y in range(len(_inp)):
    for x in range(len(_inp[0])):
        if _inp[y][x] == 'S':
            s = (x, y)
            _inp[y][x] = 'F' # TODO not always F :D


for line in _inp:
    print("".join(line))

pos = {(1, 0): ['-', '7', 'J'],
       (-1, 0):['-', 'F', 'L'],
       (0, 1): ['|', 'L', 'J'],
       (0, -1): ['|', 'F', '7']}
pos_dirs = {
    '-': [(1, 0), (-1, 0)],
    '|': [(0, 1), (0, -1)],
    'F': [(1, 0), (0, 1)],
    'J': [(-1, 0), (0, -1)],
    '7': [(-1, 0), (0, 1)],
    'L': [(1, 0), (0, -1)]
}
_not = {(1, 0): '|FL',
       (-1, 0): '|7J',
       (0, 1): '-7F',
       (0, -1): '-LJ'}

queue = [[s, 0]]
res = []
print(f"start {s}")
# jump over ; if the pieces on both sides
# can be connected otherwise they werent
# together in the first place
# which means we traverse into it for p2 finding all
# tiles
cycle_points = set()
disallowed = []
while queue:
    p, steps = queue.pop()
    cycle_points.add(p)
    for (i, j) in pos_dirs[_inp[p[1]][p[0]]]:
        cur_sign =  _inp[p[1]][p[0]]
        new = (p[0] + i, p[1] + j)
        after = (new[0] + i, new[1] + j)
        if new[0] < 0 or new[1] < 0:
            continue
        extend = False
        try:
            if (((sign := _inp[new[1]][new[0]]) in pos[(i, j)] and sign not in _not[(i, j)])
                or (extend := (sign == ';' and _inp[after[1]][after[0]] in pos[(i, j)]))):
                if extend:
                    disallowed.append(new)
                    new = after
                item = [new, (new_steps := steps + 1)]
                dont_append = False
                for it in queue + res:
                    if it[0] == new and new_steps >= it[1]:
                        dont_append = True
                if not dont_append:
                    res = [r for r in res if r[0] != new]
                    res.append(item)
                    queue.append(item)
        except IndexError:
            pass
#print(res)
print('p1', max(([x[1] for x in res])))
queue2 = set([(x, len(_inp)-1) for x in range(len(_inp[0]))]) | \
    set([(x, 0) for x in range(len(_inp[0]))]) | \
    set([(0, y) for y in range(len(_inp))]) | \
    set([(len(_inp[0])-1, y) for y in range(len(_inp))])
queue2 = {q for q in queue2 if q not in cycle_points and q not in disallowed}

print('q2', queue2)
visited = set()
outside = set()
while queue2:
    p = queue2.pop()
    visited.add(p)
    if not _inp[p[1]][p[0]] == ';':
        outside.add(p)
    for (i, j), val in pos.items():
       new = (p[0] + i, p[1] + j)
       if new[0] < 0 or new[1] < 0 or new in disallowed or new[0] >= len(_inp[0])\
            or new[1] >= len(_inp):
           continue
       
       if new not in visited and new not in cycle_points:
            queue2.add(new)

stray_pipes_out = set()
total = set()
stray_pipes = set()
for y in range(len(_inp)):
    for x in range(len(_inp[0])):
        if _inp[y][x] != ';':
            total.add((x, y))
        if _inp[y][x] in c and (x, y) in outside:
            stray_pipes_out.add((x, y))
        if _inp[y][x] in c and (x, y) not in cycle_points:
            stray_pipes.add((x, y))
stray_pipes_in_cicle = stray_pipes - stray_pipes_out

print(
    f"Total: {len(total)}, cycle points: {len(cycle_points)}, outside: {len(outside)}, stray pipes incircle {len(stray_pipes_in_cicle)}")
tiles = (total - cycle_points - outside)
print('tiles', len(tiles))

_print = False
## PRINTING
if _print:
    from copy import deepcopy
    printable = deepcopy(_inp)
    for y in range(len(printable)):
        for x in range(len(printable[0])):
            if (x, y) in outside:
                printable[y][x] = 'O'
    for x, y in tiles:
        printable[y][x] = 'I'

    for x, y in stray_pipes_in_cicle:
        printable[y][x] = 'P'

    printable = [[x for x in y if x != ';'] for y in printable]
    printable = [el for el in printable if el]

    for i, line in enumerate(printable):
        print("".join(line))


    # RUINS INPUT
    for y in range(len(_inp)):
        for x in range(len(_inp[0])):
            if (x, y) in visited:
                _inp[y][x] = 'V'
    for i, line in enumerate(_inp):
        print("".join(line))

    ## PRINTING 