import re

# improvement inspired by hb4q and adjusted to include p1
r, r2 = '1|2|3|4|5|6|7|8|9', '|one|two|three|four|five|six|seven|eight|nine'

def line_digits(r, line):
    return [*map({n: i%9+1 for i, n in enumerate(r.split('|'))}.get,
            re.findall(rf'(?=({r}))', line))]
def f(line):
    x, y = line_digits(r, line), line_digits(r+r2, line)
    return 10*x[0] + x[-1], 10*y[0] + y[-1]

print([sum(z) for z in zip(*map(f, open('d1/input.txt')))])
