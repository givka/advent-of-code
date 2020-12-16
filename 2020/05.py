L = [line.strip() for line in open("05.in").readlines()]

S = []
seat_id = 0
for line in L:
    r_min, r_max = 0, 127
    c_min, c_max = 0, 7
    for c in line:
        if c == "F":
            r_max -= (r_max - r_min) // 2 + 1
        if c == "B":
            r_min += (r_max - r_min) // 2 + 1
        if c == "L":
            c_max -= (c_max - c_min) // 2 + 1
        if c == "R":
            c_min += (c_max - c_min) // 2 + 1

    assert (r_min == r_max and c_min == c_max)
    seat_id = max(seat_id, r_min * 8 + c_min)
    S.append(r_min * 8 + c_min)

print(seat_id)

for s in range(0, seat_id):
    if s not in S and s + 1 in S and s - 1 in S:
        print(s)
