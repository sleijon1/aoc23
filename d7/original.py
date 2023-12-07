import collections as col

def type(vals):
    if 5 in vals:
        return 1
    elif 4 in vals:
        return 2
    elif 3 in vals and 2 in vals:
        return 3
    elif 3 in vals:
        return 4
    elif len([v for v in vals if v == 2]) == 2:
        return 5
    elif 2 in vals:
        return 6
    return 7

def parse(p2=False):
    cards = col.defaultdict(list)
    _map = ('AKQJT', 'EDC' + ('1' if p2 else 'B') + 'A')
    for l in open("d7/input.txt").read().translate(str.maketrans(*_map)).splitlines():
        h, b = l.split(' ')
        hc, J = {c: h.count(c) for c in h if c != '1'}, h.count('1')
        if J != 5:
            hc[max(hc, key=hc.get)] += J
        else:
            hc['1'] = J
        cards[type(hc.values())].append((h, int(b)))
    return cards

def _sort(cards):    
    sort_ranks, ranking = sorted(cards.items(), key=lambda x: x[0]), []
    for _, cds in sort_ranks:
        for c in sorted(cds, key=lambda x: x[0], reverse=True):
            ranking = [c] + ranking
    return sum([ranking[i][1] * (i+1) for i in range(0, len(ranking))])

print(_sort(parse()), _sort(parse(p2=True)))

