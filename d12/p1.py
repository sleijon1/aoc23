import collections as c
from copy import copy
import itertools
lines = open("d12/input.txt").read().splitlines()

def _match(r, p):
    r.append('.')
    rpat = []
    count = 0
    for c in r:
        if c == '#':
            count += 1
        elif c == '.' and count != 0:
            rpat.append(count)
            count = 0
    return rpat == p

combinations = c.defaultdict(int)
for i, line in enumerate(lines):
    r, p = line.split(" ")
    r = list(r)
    p = list(map(int, p.split(',')))
    uk = [k for k, el in enumerate(line) if el == '?']
    
    for pos in list(itertools.product(['#', '.'], repeat=len(uk))):
        sub = copy(r)
        for l, uki in enumerate(uk):
            sub[uki] = pos[l]
        if _match(sub, p):
            combinations[i] += 1

lst = list(itertools.product(['#', '.'], repeat=3))
print(sum(combinations.values()))

