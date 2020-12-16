L = []
for line in open("08.in").readlines():
    line = line.strip()
    com, val = line.split()
    val = int(val)
    L.append((com, val))


S = set()
acc = 0
idx = 0
while idx not in S:
    S.add(idx)
    com, val = L[idx]
    if com == "acc":
        acc += val
        idx += 1
    if com == "jmp":
        idx += val
    if com == "nop":
        idx += 1

print(acc)

C = set()
idx = 0
acc = 0
while idx != len(L):
    S = set()
    acc = 0
    idx = 0
    changed = False
    while idx not in S and idx < len(L):
        S.add(idx)
        com, val = L[idx]

        if not changed and (com == "jmp" or com == "nop") and idx not in C:
            com = "nop" if com == "jmp" else "jmp"
            C.add(idx)
            changed = True

        if com == "acc":
            acc += val
            idx += 1
        if com == "jmp":
            idx += val
        if com == "nop":
            idx += 1
print(acc)
