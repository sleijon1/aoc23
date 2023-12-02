import re, copy

# improvement inspired by fuglede and adjusted

cnt = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
with open("d1/input.txt") as f:
    data = f.read().splitlines()
    data2 = copy.deepcopy(data)
    for i, _ in enumerate(data2):
        for j, c in enumerate(cnt):
            data2[i] = data2[i].replace(c, f'{c}{j+1}{c}')

def calibration(ls):
    ns = [re.findall("\d", x) for x in ls]
    return sum(int(n[0] + n[-1]) for n in ns)


print(calibration(data), calibration(data2))
