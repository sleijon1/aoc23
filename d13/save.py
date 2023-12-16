
def v_ref(lines):
    length = len(lines[0])
    s_upper = length // 2
    print(f"s_upper {s_upper}")
    for s in  range(1, s_upper):
        for i in range(len(lines[0])):
            try:
                match = []
                for line in lines:
                    match.append(line[i:i+s] == line[i+s:i+2*s][::-1])
                if all(match):
                    return len(lines[0][:i]) + 1
            except IndexError:
                continue
    return 0

def transform(lines):
    new_lines = []
    for x in range(len(lines[0])):
        new_lines.append([line[x] for line in lines])
    return new_lines

pats = open('d13/input.txt').read().split('\n\n')
v = sum([v_ref([l for l in pat.splitlines()]) for pat in pats])
h = sum([100*v_ref([l for l in transform(pat.splitlines())]) for pat in pats])
print(v+h)