commands = [aa.strip() for aa in open("02.in").readlines()]

pos = [0, 0]
res = ""
D = ["123", "456", "789"]

for c in commands:
    for l in c:
        if l == 'U' and pos[1] != -1:
            pos[1] -= 1
        if l == 'D' and pos[1] != 1:
            pos[1] += 1
        if l == 'R' and pos[0] != 1:
            pos[0] += 1
        if l == 'L' and pos[0] != -1:
            pos[0] -= 1
    res += str(D[pos[1]+1][pos[0]+1])

print(res)


pos = [-2, 0]
res = ""
D = ["  1  ", " 234 ", "56789", " ABC ", "  D  "]

for c in commands:
    for l in c:
        if l == 'U' and abs(pos[0]) < 2 and not (abs(pos[0]) == 1 and pos[1] == -1) and pos[1] != -2:
            pos[1] -= 1
        if l == 'D' and abs(pos[0]) < 2 and not (abs(pos[0]) == 1 and pos[1] == 1) and pos[1] != 2:
            pos[1] += 1
        if l == 'R' and abs(pos[1]) < 2 and not (abs(pos[1]) == 1 and pos[0] == 1) and pos[0] != 2:
            pos[0] += 1
        if l == 'L' and abs(pos[1]) < 2 and not (abs(pos[1]) == 1 and pos[0] == -1) and pos[0] != -2:
            pos[0] -= 1
    res += str(D[pos[1]+2][pos[0]+2])

print(res)
