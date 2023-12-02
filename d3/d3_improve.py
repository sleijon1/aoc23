import collections as c, math as m, re

parts = c.defaultdict(list)
board = list(open('d3/input.txt'))
chars = {(r, c) for r in range(len(board)) for c in range(len(board))
                if board[r][c] not in '01234566789.'}

for r, row in enumerate(board):
    for n in re.finditer(r'\d+', row):
        edge = {(r, c) for r in (r-1, r, r+1)
                       for c in range(n.start()-1, n.end()+1)}
        # assumes numbers adj to only one symbol, could easily be wrong.
        # you would have to track which symbols it hits for p2 and
        # make sure to not double count. hard assumptions
        for o in edge & chars:
            parts[o].append((board[o[0]][o[1]], int(n.group(0))))

print(sum(sum([p    for _, p in l]) for l in parts.values()),
      sum(m.prod([p for s, p in l if len(l)==2 and s == '*']) for l in parts.values()))

# once again, inspiration from hb4q but adjusted to not make
# assumptions:
# 1. that only * will have 2 adjacent nums
# and (2.) laxed 140x140 to square matrix