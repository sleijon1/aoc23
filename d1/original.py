mapping = {"one": '1', "two": '2', "three": '3', 
           "four": '4', "five": '5', "six": '6',
           "seven": '7', "eight": '8', "nine": '9'}

def find_int(line, reverse=False):
    parsed = ""
    for char in line:
        for key in mapping:
            if key in parsed:
                return mapping[key] 
        try:
            int(char)
            return char
        except Exception:
            if reverse:
                parsed = char + parsed
            else:
                parsed += char

sum = 0
for line in open("d1/input.txt").readlines():
    d1, d2 = find_int(line), find_int(line[::-1], reverse=True)
    sum += int(d1+d2)
print(sum)
