import math as m, re

inp = re.findall(r'(\d+)', open('d6/input.txt').read())
p1 = [[int(inp[i]), int(inp[4:][i])] for i in range(len(inp)//2)]
p2 = [int(''.join(inp[:4])), int(''.join(inp[4:]))]

def parabola_points(t, d):
    r1, r2 = t/2 + m.sqrt(t**2/4 - d), t/2 - m.sqrt(t**2/4 - d)
    return len(range(m.ceil(r1), m.ceil(r2), -1)) - int(m.ceil(r1) == r1)

print(m.prod([parabola_points(*p) for p in p1]), parabola_points(*p2))
