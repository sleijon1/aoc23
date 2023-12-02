import math
numbers, symbols = {}, {}
number = ''
for y, line in enumerate(t := open('d3/input.txt').read().splitlines()):
    for x, char in enumerate(line):
        try:
            int(char)
            number += char
        except ValueError:
            if char != '.':
                symbols[x, y] = char
            if number:
                numbers[x-1, y] = number
                number = ''
    if number:
        numbers[x, y] = number
        number = ''
            

p1 = 0
gears = {gp: [] for gp, symb in symbols.items() if symb == '*'}
for p in numbers:
    try:
        for y in range(max(p[1]-1, 0), p[1]+2):
            for x in range(max(p[0]-len(numbers[p]), 0), p[0]+2):
                if (x, y) in symbols.keys():
                    p1 += int(numbers[p])
                    if (x, y) in gears:
                        gears[x, y].append(int(numbers[p]))
                    raise Exception("break loop")
    except Exception as e:
        pass

print(p1, sum([math.prod(vals) for vals in gears.values() if len(vals) == 2]))

# not cleaned up