from copy import deepcopy

LL = [list(l.strip()) for l in open("11.in").readlines()]
D = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
L = deepcopy(LL)


def process(L: list):
    LC = deepcopy(L)

    for y in range(len(L)):
        for x in range(len(L[0])):
            val = L[y][x]
            if val == 'L':
                adj = False
                for xx, yy in D:
                    if 0 <= x+xx < len(L[0]) and 0 <= y+yy < len(L):
                        if L[y+yy][x+xx] == "#":
                            adj = True
                            break
                if not adj:
                    LC[y][x] = "#"
            elif val == '#':
                occ = 0
                for xx, yy in D:
                    if 0 <= x+xx < len(L[0]) and 0 <= y+yy < len(L):
                        if L[y+yy][x+xx] == "#":
                            occ += 1
                if occ >= 4:
                    LC[y][x] = "L"

    return LC


while True:
    M = process(L)
    if M == L:
        print(sum([1 for l in M for c in l if c == "#"]))
        break
    else:
        L = M


L = deepcopy(LL)


def process2(L: list):
    LC = deepcopy(L)

    for y in range(len(L)):
        for x in range(len(L[0])):
            val = L[y][x]
            if val == 'L':
                adj = False
                for xx, yy in D:
                    dx,dy = xx,yy
                    while 0 <= x+xx < len(L[0]) and 0 <= y+yy < len(L) and L[y+yy][x+xx] == ".":
                        xx += dx
                        yy += dy
                    if 0 <= x+xx < len(L[0]) and 0 <= y+yy < len(L) and L[y+yy][x+xx] == "#":
                        adj = True
                        break
                if not adj:
                    LC[y][x] = "#"
            elif val == '#':
                occ = 0

                for xx, yy in D:
                    dx,dy = xx,yy
                    while 0 <= x+xx < len(L[0]) and 0 <= y+yy < len(L) and L[y+yy][x+xx] == ".":
                        xx += dx
                        yy += dy
                    if 0 <= x+xx < len(L[0]) and 0 <= y+yy < len(L):
                        if L[y+yy][x+xx] == "#":
                            occ += 1
                if occ >= 5:
                    LC[y][x] = "L"

    return LC


while True:
    M = process2(L)
    if M == L:
        print(sum([1 for l in M for c in l if c == "#"]))
        break
    else:
        L = M
