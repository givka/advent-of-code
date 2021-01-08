from collections import defaultdict

L = [line.strip() for line in open("24.in")]
D = [("e", (1, 0)), ("se", (0.5, -1)), ("sw", (-0.5, -1)),
     ("w", (-1, 0)), ("nw", (-0.5, 1)), ("ne", (0.5, 1))]

M = defaultdict(lambda: 0)
for line in L:
    x, y = 0, 0
    while len(line):
        for d, (dx, dy) in D:
            if line.startswith(d):
                x, y = x+dx, y+dy
                line = line[len(d):]
                break
    M[(x, y)] += 1

print(len([m for m in M if M[m] % 2 == 1]))

S = set()
for m in M:
    if M[m] % 2 == 1:
        S.add(m)

for i in range(100):
    SS = set()
    for (x,y) in S:
        c = 0
        for (d, (dx,dy)) in D:
            if (x+dx, y+dy) in S:
                c+=1
        if c==0 or c>2:
            pass
        else:
            SS.add((x,y))

        for (d, (dx,dy)) in D:
            if (x+dx, y+dy) not in S:
                c=0
                for (dd, (ddx,ddy)) in D:
                    if (x+dx+ddx, y+dy+ddy)  in S:
                        c+=1
                if c==2:
                    SS.add((x+dx,y+dy))
    S = SS

print(len(S))
