from collections import defaultdict

M = defaultdict(lambda: ".")

x, y, z = 0, 0, 0

for line in open("17.in").readlines():
    line = line.strip()
    x = 0
    for c in line:
        M[(x, y, z)] = c
        x += 1
    y += 1


for i in range(6):
    min_x = min(M.keys(), key=lambda x: x[0])[0]
    max_x = max(M.keys(), key=lambda x: x[0])[0]
    min_y = min(M.keys(), key=lambda x: x[1])[1]
    max_y = max(M.keys(), key=lambda x: x[1])[1]
    min_z = min(M.keys(), key=lambda x: x[2])[2]
    max_z = max(M.keys(), key=lambda x: x[2])[2]

    MM = M.copy()
    for x in range(min_x-1, max_x+1+1):
        for y in range(min_y-1, max_y+1+1):
            for z in range(min_z-1, max_z+1+1):
                ans = 0
                for xx in range(-1, 2):
                    for yy in range(-1, 2):
                        for zz in range(-1, 2):
                            if xx == yy == zz == 0:
                                continue
                            ans += 1 if M[(x+xx, y+yy, z+zz)] == "#" else 0
                if M[(x, y, z)] == "#" and ans not in [2, 3]:
                    MM[(x, y, z)] = "."
                elif M[(x, y, z)] == "." and ans == 3:
                    MM[(x, y, z)] = "#"

    M = MM

print(sum(1 for m in MM.values() if m == "#"))


M = defaultdict(lambda: ".")

x, y, z, w = 0, 0, 0, 0

for line in open("17.in").readlines():
    line = line.strip()
    x = 0
    for c in line:
        M[(x, y, z, w)] = c
        x += 1
    y += 1


for i in range(6):
    min_x = min(M.keys(), key=lambda x: x[0])[0]
    max_x = max(M.keys(), key=lambda x: x[0])[0]
    min_y = min(M.keys(), key=lambda x: x[1])[1]
    max_y = max(M.keys(), key=lambda x: x[1])[1]
    min_z = min(M.keys(), key=lambda x: x[2])[2]
    max_z = max(M.keys(), key=lambda x: x[2])[2]
    min_w = min(M.keys(), key=lambda x: x[3])[3]
    max_w = max(M.keys(), key=lambda x: x[3])[3]

    MM = M.copy()
    for x in range(min_x-1, max_x+1+1):
        for y in range(min_y-1, max_y+1+1):
            for z in range(min_z-1, max_z+1+1):
                for w in range(min_w-1, max_w+1+1):
                    ans = 0
                    for xx in range(-1, 2):
                        for yy in range(-1, 2):
                            for zz in range(-1, 2):
                                for ww in range(-1, 2):
                                    if xx == yy == zz == ww == 0:
                                        continue
                                    ans += 1 if M[(x+xx, y+yy,
                                                   z+zz, w+ww)] == "#" else 0

                    if M[(x, y, z, w)] == "#" and ans not in [2, 3]:
                        MM[(x, y, z, w)] = "."
                    elif M[(x, y, z, w)] == "." and ans == 3:
                        MM[(x, y, z, w)] = "#"
    M = MM

print(sum(1 for m in MM.values() if m == "#"))
