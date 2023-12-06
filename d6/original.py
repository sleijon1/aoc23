import math as m, re

inp = re.findall(r':*.(\d+)', open('d6/input.txt').read(), re.MULTILINE)
p1 = {int(inp[i]): int(inp[4:][i]) for i in range(len(inp)//2)}
p2 = {int(''.join(inp[:4])): int(''.join(inp[4:]))}

def count_wins(record):
    races = []
    for time, dist in record.items():
        wins = 0
        for hold_time in range(1, (time+1)//2):
            if (time - hold_time) * hold_time > dist:
                wins += 1
        races.append(2*wins + (1 if time % 2 == 0 else 0))
    return m.prod(races)
print(count_wins(p1), count_wins(p2))
