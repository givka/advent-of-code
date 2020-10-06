commands = open("01.in").readline().strip().split(", ")

D = [[0, 1], [1, 0], [0, -1], [-1, 0]]
cur_index = 0
cur_pos = [0, 0]


for c in commands:
    cur_index = (cur_index + 1) % 4 if c[0] == 'R' else (cur_index - 1) % 4
    cur_pos[0] += int(c[1:])*D[cur_index][0]
    cur_pos[1] += int(c[1:])*D[cur_index][1]

print(cur_pos, abs(cur_pos[0])+abs(cur_pos[1]))

cur_index = 0
cur_pos = [0, 0]
M = {}
Found = False
M[tuple(cur_pos)] = True

for c in commands:
    cur_index = (cur_index + 1) % 4 if c[0] == 'R' else (cur_index - 1) % 4
    for i in range(int(c[1:])):
        cur_pos[0] += D[cur_index][0]
        cur_pos[1] += D[cur_index][1]
        if tuple(cur_pos) in M:
            Found = True
            break
        M[tuple(cur_pos)] = True

    if Found:
        break

print(cur_pos, abs(cur_pos[0])+abs(cur_pos[1]))
