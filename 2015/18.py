from collections import defaultdict


def stick_lights(D):
    D[0, 0] = "#"
    D[size-1, 0] = "#"
    D[0, size-1] = "#"
    D[size-1, size-1] = "#"


def tick(D):
    DD = D.copy()
    for y in range(size):
        for x in range(size):
            count = 0
            for yy in range(-1, 1+1):
                for xx in range(-1, 1+1):
                    if xx == 0 and yy == 0:
                        continue
                    if D[x+xx, y+yy] == "#":
                        count += 1
            if D[x, y] == "#":
                if count != 2 and count != 3:
                    DD[x, y] = "."
            else:
                if count == 3:
                    DD[x, y] = "#"
    return DD


D = defaultdict(lambda: ".", {})

x, y = 0, 0
for l in open("18.in").readlines():
    x = 0
    for c in l.strip():
        D[(x, y)] = c
        x += 1
    y += 1


size = y
step = 100

D1 = D.copy()
for i in range(step):
    D1 = tick(D1)
print(len([d for d in D1.values() if d == "#"]))

D2 = D.copy()
stick_lights(D2)
for i in range(step):
    D2 = tick(D2)
    stick_lights(D2)
print(len([d for d in D2.values() if d == "#"]))
