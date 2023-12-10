_inp = open("d10/input.txt").read().splitlines()
_inp = [list(string) for string in _inp]
_inp = [list(';'.join(r)) for r in _inp]
x_arr = [list(';'*len(_inp[0])) for _ in _inp]
new_inp = []
for i in range(len(_inp)):
    new_inp.append(_inp[i])
    new_inp.append(x_arr[i])
_inp = new_inp

print(_inp)
s = None
c = '|-JL7F'
for y in range(len(_inp)):
    for x in range(len(_inp[0])):
        if _inp[y][x] == 'S':
            s = (x, y)
            _inp[y][x] = 'F' # TODO

for i, line in enumerate(_inp):
    print(i, "".join(line))
pos = {(1, 0): ['-', '7', 'J'],
       (-1, 0):['-', 'F', 'L'],
       (0, 1): ['|', 'L', 'J'],
       (0, -1): ['|', 'F', '7']}

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
    #print('p', p)
    for (i, j), val in pos.items():
        cur_sign =  _inp[p[1]][p[0]]
        new = (p[0] + i, p[1] + j)
        after = (new[0] + i, new[1] + j)
        if new[0] < 0 or new[1] < 0:
            continue
        #print(f'new {new} after {after}')
        extend = False
        try:
            if (((sign := _inp[new[1]][new[0]]) in val and sign not in _not[(i, j)])
                or (extend := (sign == ';' and _inp[after[1]][after[0]] in val))):
                #print("money moves")
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
                    #print('appending', item)
                    queue.append(item)
        except IndexError:
            #print('ie')
            pass
#print(res)
print(max(([x[1] for x in res])))
# Traverse every point that is not in the cycle by walking around
# transform input by putting X between pipes
## part 2
# TODO set comprehension

queue2 = set([(0, 0), (0, len(_inp)-1), (len(_inp[0])-1, 0)])
#queue2 = set(queue2) - stray_pipes - cycle_points
print('q2', queue2)
visited = set()
outside = set()
while queue2:
    p = queue2.pop()
    visited.add(p)
    if not _inp[p[1]][p[0]] == ';':
        outside.add(p)
    for (i, j), val in pos.items():
       #cur_sign =  _inp[p[1]][p[0]]
       new = (p[0] + i, p[1] + j)
       #after = (new[0] + i, new[1] + j)
       if new[0] < 0 or new[1] < 0 or new in disallowed:
           continue
       try:
           if new not in visited and _inp[new[1]][new[0]] in '.;':
               #print(new)
               queue2.add(new)
       except IndexError:
           #print('ie')
           pass
print(len(outside))
print(outside)
stray_pipes = set()
total = set()
for y in range(len(_inp)):
    for x in range(len(_inp[0])):
        if _inp[y][x] != ';':
            total.add((x, y))
        if _inp[y][x] in c and (x, y) not in cycle_points and (x, y) not in outside:
            stray_pipes.add((x, y))


# total - cycle nodes - outside - all pipes not in cycle
print(
    f"Total: {len(total)}, cycle points: {len(cycle_points)}, outside: {len(outside)}, stray pipes {len(stray_pipes)}")
print(len(total - cycle_points - outside - stray_pipes))

## PRINTING
from copy import deepcopy
printable = deepcopy(_inp)
for y in range(len(printable)):
    for x in range(len(printable[0])):
        if (x, y) in outside:
            printable[y][x] = 'O'
for x, y in (total - cycle_points - outside - stray_pipes):
    printable[y][x] = 'I'

printable = [[x for x in y if x != ';'] for y in printable]
printable = [el for el in printable if el]

for i, line in enumerate(printable):
    print("".join(line))
## PRINTING