G = 4000000

with open('input.txt', 'r') as fin:
    t = fin.read().split('\n')

inp = []
for sbr in t:
    sbr = sbr.replace('Sensor at x=', '').replace(', y=', ' ').replace(': closest beacon is at x=', ' ')
    x, y, a, b = list(map(int, sbr.split()))
    inp.append((x, y, a, b))

for sy in range(G + 1):
    sl = []
    for x, y, a, b in inp:
        d = abs(x - a) + abs(y - b)
        if abs(y - sy) > d:
            continue
        sl.append((x - (d - abs(y - sy)), -1))    
        sl.append((x + (d - abs(y - sy)) + 1, +1))
    sl.append((0, 2))
    sl.append((G, 2))
    sl.sort()
    cntr = 0
    for sx, tt in sl:
        cntr -= tt if tt in [-1, 1] else 0
        if cntr == 0 and 0 <= sx <= G:
            print(sx, sy, sx*4000000+sy)

    if sy % 100000 == 0:
        print('checking y =', sy)