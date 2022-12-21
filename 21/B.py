with open('input.txt', 'r') as fin:
    t = fin.read().split('\n')

d = {t[i].split(': ')[0]: t[i].split(': ')[1] for i in range(len(t))}
l = -10**30
r = 10**30

def solve(v, h):
    c = d[v]
    if v == 'humn':
        return h
    if ' ' not in c:
        return int(c)
    a = solve(c[:4], h)
    b = solve(c[7:], h)
    if '+' in c:
        return a + b
    elif '-' in c:
        return a - b
    elif '*' in c:
        return a * b
    elif '/' in c:
        return a / b

for i in range(1000):
    m = (l + r) / 2
    res = solve('root', m)
    if res < 0:
        r = m
    else:
        l = m

print(l, solve('root', l))