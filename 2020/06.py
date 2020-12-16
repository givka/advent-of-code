lines = open("06.in").readlines()
L = []
S = set()
ans = 0

for line in lines:
    line = line.strip()

    if line == "":
        ans += len(S)
        S = set()
        continue

    for c in line:
        S.add(c)

ans += len(S)
print(ans)

L = []
S = set()
C = []
ans = 0
for line in lines:
    line = line.strip()

    if line == "":

        for s in S:
            if all(s in c for c in C):
                ans += 1

        S = set()
        C = []
        continue

    for c in line:
        S.add(c)
    C.append(line)

for s in S:
    if all(s in c for c in C):
        ans += 1
print(ans)
