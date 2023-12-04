import re, functools

win_num = {}
for card, l in re.findall(r' *(\d+): (.*)', open("d4/input.txt").read()):
    c, w  = [set(map(int, [n for n in s.split(' ') if n])) for s in l.split(' | ')]
    win_num[int(card)] = len(c & w)

@functools.cache
def count_cards(card, count=1):
    new_count = count
    for next_card in range(card + 1, card + 1 + win_num[card]):
        new_count += count_cards(next_card, count=count)
    return new_count

print(sum([2**(w-1) for w in win_num.values() if w]),
      sum([count_cards(k) for k in win_num]))
