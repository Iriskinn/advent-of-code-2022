with open('input.txt', 'r') as fin:
    t = fin.read().split('\n')[:-1]

d = ['=', '-', '0', '1', '2']

def to_num(s):
    res = 0
    for i in range(len(s)):
        res = 5 * res + (d.index(s[i]) - 2)
    return res

def to_enc(x):
    ans = []
    while x > 0:
        ans.append(d[((x % 5) + 2) % 5])
        if x % 5 > 2:
            x += 5
        x //= 5
    return ''.join(ans[::-1])

x = sum(list(map(to_num, t)))
print(to_enc(x))