from copy import deepcopy

def v_ref(lines, h, flip=False):
    length = len(lines[0])
    for i in range(0, length):
        wrong_i = False
        for line in lines:
            s = len(line[i:]) // 2
            if not s or not line[i:i+s] == line[i+s:][::-1]:
                wrong_i = True
                break
        if not wrong_i:
            if flip:
                return [length - s - i, (i, s, flip, h)]
            return [len(line[:i+s]), (i, s, flip, h)]
    return [0, 'lol']


def transform(lines):
    new_lines = []
    for x in range(len(lines[0])):
        new_lines.append([line[x] for line in lines])
    return new_lines


def flip(lines):
    return [line[::-1] for line in lines]


def test_smudge(pattern):
    copy = deepcopy(pattern)
    reverse = {'.': '#', '#': '.'}
    for y in range(len(copy)):
        for x in range(len(copy[0])):
            copy[y][x] = reverse[copy[y][x]]
            yield copy
            copy[y][x] = reverse[copy[y][x]]

from collections import defaultdict
original_reflections = defaultdict()
def sum_refs(pat, pat_i, original=True):
    a = v_ref(pat, h=False)
    b = v_ref(flip(pat), flip=True, h=False)
    c = v_ref(transform(pat), h=True)
    d = v_ref(flip(transform(pat)), flip=True, h=True)
    rs = [v[1] for v in [a, b, c, d] if v[1] != 'lol']
    if original:
        original_reflections[pat_i] = rs[0]
    else:
        for rs in [a, b, c, d]:
            if rs[1] == original_reflections[pat_i]:
                rs[0] = 0
    return sum([a[0], b[0], 100*c[0], 100*d[0]])


pats = open('d13/input.txt').read().split('\n\n')
t, p2 = 0, 0
for pat_i, o in enumerate(pats):
    lines = [list(line) for line in o.splitlines()]
    t += sum_refs(lines, pat_i=pat_i, original=True)
    for new in test_smudge(lines):
        smudge = sum_refs(new, pat_i=pat_i, original=False)
        p2 += smudge
        if smudge:
            break

print(t, p2)
