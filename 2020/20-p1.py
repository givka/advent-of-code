from collections import defaultdict
import math

D = {}
L = [l.strip() for l in open("20.0").readlines()]

for line in L:
    if line.startswith("Tile"):
        num = int(line.split()[1].replace(":", ""))
        D[num] = []
    elif line:
        D[num].append(list(line))


def col(i, arr):
    return [a[i] for a in arr]


S = {}
for d in D:
    S[d] = list()

for d in D:
    for dd in D:
        if dd == d:
            continue

        K = [D[d][0], D[d][-1], col(0, D[d]), col(-1, D[d])]
        K.extend([list(reversed(k)) for k in K])
        KK = [D[dd][0], D[dd][-1], col(0, D[dd]), col(-1, D[dd])]
        KK.extend([list(reversed(kk)) for kk in KK])

        found = False
        for k in K:
            for kk in KK:
                if k == kk:
                    S[d].append(dd)
                    found = True
                    break
            if found:
                break

print(S)
print(math.prod(s for s in S if len(S[s]) == 2))
