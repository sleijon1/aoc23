lines = [list(el) for el in open("d14/input.txt").read().splitlines()]

def roll_all(lines):
    rocks = ((x, y) for y in range(len(lines)) for x in range(len(lines[0]))
            if lines[y][x] == 'O')
    for x, y in rocks:
        for ny in range(y-1, -1, -1):
            if lines[ny][x] in '#O-':
                lines[y][x] = '.'
                lines[ny+1][x] = 'O'
                break
    return lines

def rotate(lines):
    new_lines = []
    for x in range(len(lines[0])):
        new_lines.append([lines[y][x] for y in range(len(lines)-1, -1, -1)])
    return new_lines

def calculate_load(lines):
    rocks = ((x, y) for y in range(len(lines)) for x in range(len(lines[0]))
             if lines[y][x] == 'O')
    load = 0
    for _, y in rocks:
        load += len(lines)-y-1
    return load
    
loads = []
def cycle_roll(n=0):
    rolled = lines
    for _ in range(n):
        for _ in range(4):
            rolled = roll_all(rolled)
            rolled = rotate(rolled)
        loads.append(calculate_load(rolled))

cycle_roll(n=1000)
try:
    for cycle_size in range(2, 100):
        for i in range(0, len(loads)):
            if loads[i:i+cycle_size] == loads[i+cycle_size:i+2*cycle_size]:
                cycle = loads[i:i+cycle_size]
                raise Exception()
except Exception:
    print('p2', cycle[(1000000000-i-1) % cycle_size])

print(f"p1 {calculate_load(lines)}")