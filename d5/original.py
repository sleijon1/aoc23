groups = open("d5/input.txt").read().split('\n\n')
seeds = list(map(int, groups[0].split(": ")[1].split(" ")))
groups = groups[1:]

mapping = {}

# data  parsing
for i, group in enumerate(groups):
    _, vals = group.split(':\n')
    ranges = vals.split('\n')
    mapping[i] = []
    for r in ranges:
        m1, m2, steps = map(int, r.split(" "))
        mapping[i].append(((m1, m1+steps), (m2, m2+steps)))

range_seeds = []
for i in range(0, len(seeds)-1, 2):
    range_seeds.append((seeds[i], seeds[i] + seeds[i+1]))

# seed->location or reverse for p2
def path(start_val, r=False):
    direction = range(len(groups)-1, -1, -1) if r else range(len(groups))
    for j in direction:
        tar_i = 0
        for k in mapping[j]:
            rt, rs = k[::-1] if r else k
            if rs[0] <= start_val < rs[1]:
                tar_i  = start_val - rs[0]
                start_val = rt[0] + tar_i
                break
    return start_val

def calcmin2(attempt=0):
    while True:
        location = path(attempt, r=True)
        for r1, r2 in range_seeds:
            if r1 <= location < r2:
                return attempt
        attempt += 1

print('p2', calcmin2(), 'p1', min(path(seeds[i]) for i in range(len(seeds))))

