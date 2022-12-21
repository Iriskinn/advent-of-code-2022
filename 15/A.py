G = 4000000

with open('input.txt', 'r') as fin:
    t = fin.read().split('\n')[:-1]

inp = []
exc = set([])
for sbr in t:
    sbr = sbr.replace('Sensor at x=', '').replace(', y=', ' ').replace(': closest beacon is at x=', ' ')
    x, y, a, b = list(map(int, sbr.split()))
    d = abs(x - a) + abs(y - b)
    inp.append((x, y, a, b, d))
    if b == G // 2:
        exc.add(a)

for sy in [G // 2]:
    sl = [(x - (d - abs(y - sy)), -1) for x, y, a, b, d in inp if abs(y - sy) <= d]
    sr = [(x + (d - abs(y - sy)) + 1, +1) for x, y, a, b, d in inp if abs(y - sy) <= d]
    sl.extend(sr)
    sl.append((0, 2))
    sl.append((G, 2))
    sl.sort()
    cntr, st, res = 0, 0, 0
    for sx, tt in sl:
        cntr -= tt if tt in [-1, 1] else 0
        if cntr == 1 and tt == -1:
            st = sx
        elif cntr == 0 and tt == 1:
            res += sx - st
    print(res - len(exc))