from collections import defaultdict

L = [line.strip() for line in open("21.in").readlines()]
D = defaultdict(set)
I = []
R = []

for line in L:
    i, a = line.split("(contains ")
    a = a.replace(")", "")
    a = [aa.strip() for aa in a.split(",")]
    i = [ii.strip() for ii in i.split()]
    R.append((i, a))
    I.extend(i)

    for aa in a:
        S = set()
        for ii in i:
            S.add(ii)
        D[aa] = D[aa] & S if len(D[aa]) else S

res = 0
for ing in set(I):
    v = any(ing in D[k] for k in D)
    if not v:
        res += I.count(ing)
print(res)

DD = dict()
while len(D):
    for a, i in list(D.items()):
        if len(i) == 1:
            val = list(i)[0]
            for aa, ii in list(D.items()):
                if a == aa or val not in ii:
                    continue
                ii.remove(val)
            DD[a] = i
            del D[a]


D = list(DD.items())
D = list(sorted(D, key=lambda x: x[0]))
print(",".join(list(d[1])[0]for d in D))
