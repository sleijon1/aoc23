import collections, math, re

# improved from my original, took hb4q's solution and
# added part 1

def f(line):
    total = {'red': 12, 'green': 13, 'blue': 14}
    game_id = int(re.findall(r'Game (\d+):', line)[0])
    bag = collections.defaultdict(int)
    for num, col in re.findall(r'(\d+) (\w+)', line):
        if total[col] < int(num):
            game_id = 0
        bag[col] = max(bag[col], int(num))
    return math.prod(bag.values()), game_id

print([sum(x) for x in zip(*map(f, open('d2/input.txt')))])
