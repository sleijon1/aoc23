def type(hand):
    return sorted(map(hand.count, hand), reverse=True)

def parse(p2=False):
    ranking = []
    _map = ('AKQJT', 'EDC' + ('1' if p2 else 'B') + 'A')
    for l in open("d7/input.txt").read().translate(str.maketrans(*_map)).splitlines():
        h, b = l.split(' ')
        opt = max(type(h.replace('1', c)) for c in h)
        ranking.append((opt, h, int(b)))
    return ranking

def _sort(cards):
    return sum([bid * r for r, (*_, bid) in enumerate(sorted(cards), start=1)])

print(_sort(parse()), _sort(parse(p2=True)))

