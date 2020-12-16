import math
C = []
for l in open("12.in").readlines():
    l = l.strip()
    C.append((l[0], int(l[1:])))

M = [(0, 1), (1, 0), (0, -1), (-1, 0)]
idx = 1
x, y = 0, 0

for c, n in C:
    if c == "N":
        y += n
    elif c == "S":
        y -= n
    elif c == "E":
        x += n
    elif c == "W":
        x -= n
    elif c == "R":
        idx = (idx+n//90) % 4
    elif c == "L":
        idx = (idx-n//90) % 4
    elif c == "F":
        xx, yy = M[idx]
        x += n*xx
        y += n*yy

print(abs(x)+abs(y))

idx = 1
x, y = 0, 0
wx, wy = 10, 1


def rot2(x, y, a):
    a = math.radians(a)
    cosa = int(math.cos(a))
    sina = int(math.sin(a))
    return x*cosa+y*sina, -(x*sina+y*cosa) # why -y?


for c, n in C:
    if c == "N":
        wy += n
    elif c == "S":
        wy -= n
    elif c == "E":
        wx += n
    elif c == "W":
        wx -= n
    elif c == "R":
        for i in range(n//90):
            wx, wy = rot2(wx, wy, 90)
    elif c == "L":
        for i in range(n//90):
            wx, wy = rot2(wx, wy, -90)
    elif c == "F":
        x += n*wx
        y += n*wy

print(abs(x)+abs(y))
