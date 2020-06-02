M = [c for c in open('03.in').readline()]

P = set()
pos1 = (0, 0)
pos2 = (0, 0)
P.add(pos1)
P.add(pos2)

i = 0
for m in M:
    dx = 0
    dy = 0
    if m == '<':
        dx = -1
    if m == '>':
        dx = 1
    if m == 'v':
        dy = 1
    if m == '^':
        dy = -1

    if i % 2 == 0:
        pos1 = (pos1[0] + dx, pos1[1] + dy)
        P.add(pos1)
    else:
        pos2 = (pos2[0] + dx, pos2[1] + dy)
        P.add(pos2)
    i += 1

print(len(P))
