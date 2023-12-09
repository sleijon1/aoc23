_inp = [[int(d) for d in line.split(" ")] for line in 
        open("d9/input.txt").read().splitlines()]

def find_next(h, t=False):
    if all([v == 0 for v in h]):
        return h[-1]
    n = find_next([h[i+1] - h[i] for i in range(len(h)-1)], t=t)
    return (n + h[-1]) if not t else (h[0] - n)

print(sum([find_next(h) for h in _inp]), sum([find_next(h, t=True) for h in _inp]))