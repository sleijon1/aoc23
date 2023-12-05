import re, functools, copy as c

win_num = {}
for card, l in re.findall(r' *(\d+): (.*)', open("d4/input.txt").read()):
    c, w  = [set(map(int, [n for n in s.split(' ') if n])) for s in l.split(' | ')]
    win_num[int(card)] = len(c & w)

N = [1]*len(win_num)
for i, n in enumerate(N):
    for j in range(win_num[i+1]):
        N[i + j + 1] += N[i]

print(sum([2**(w-1) for w in win_num.values() if w]),
      sum(N))

# inspiration from looking at reddit, no particular solutions, just made
# me realize recursion wasnt needed here