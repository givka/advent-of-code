from collections import defaultdict

D = defaultdict(list)
M = None
molecule = False
for line in open("19.in").readlines():
    line = line.strip()
    if not line:
        molecule = True
    elif molecule:
        M = line
    else:
        k, v = line.split(" => ")
        D[k].append(v)

if not M:
    M = "HOHOHO"

L = list()
for k in D:
    for v in D[k]:
        for i in range(len(M)):
            if M[i:i+len(k)] == k:
                L.append(M[:i]+v+M[i+len(k):])

print(len(set(L)))
