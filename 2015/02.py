from collections import namedtuple

Box = namedtuple('Box', 'l w h')

G = [l.strip().split('x') for l in open('02.in').readlines()]
G = [Box(int(l[0]), int(l[1]), int(l[2])) for l in G]

res = 0
for g in G:
    s = sorted(g)
    res += 2 * g.l * g.w + 2 * g.w * g.h + 2 * g.h * g.l
    res += s[0] * s[1]
print(res)

res = 0
for g in G:
    s = sorted(g)
    res += s[0] + s[0] + s[1] + s[1]
    res += s[0] * s[1] * s[2]
print(res)