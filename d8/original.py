import re, math as m
instr, nodes = open("d8/input.txt").read().split('\n\n')
instr = instr.replace('L', '0').replace('R', '1')
nodes = {n: (l, r) for n, l, r in re.findall(r"(\w+) = \((\w+), (\w+)\)", nodes)}

def find_z(start):
    i = 0
    t = True
    sn = start
    while not start[-1] == 'Z' or t:
        t = False
        instruction = int(instr[i % len(instr)])
        start = nodes[start][instruction]
        i += 1
    print(sn, start, i)
    return i


a_starts = [k for k in nodes if k[-1] == 'A']
print(find_z('AAA'), a_lcm := m.lcm(*map(find_z, a_starts)))

z_starts = [k for k in nodes if k[-1] == 'Z']
print(z_lcm := m.lcm(*map(find_z, z_starts)))

print(a_lcm == z_lcm)

print([s % len(instr) == 0 for s in map(find_z, a_starts)])