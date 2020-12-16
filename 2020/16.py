from collections import defaultdict

n      = 0
N      = []
F      = []
ticket = None
for line in open("16.in").readlines():
    line = line.strip()
    if line:
        if line.startswith("your ticket"):
            n=-1
            continue
        if line.startswith("nearby tickets"):
            continue
        if n==0:
            name, line = line.split(":")
            line = line.split("or")
            line = [l.strip() for l in line]
            line = [tuple(map(int,l.split("-"))) for l in line]
            F.append((name,line))
        elif n==-1:
            ticket = tuple(map(int,line.split(",")))
            n      = 1
        elif n==2:
            N.append(tuple(map(int,line.split(","))))
    else:
        n+=1

FF = [ff for (_,f) in F for ff in f]
NN = [nn for n in N for nn in n]

res = 0
for n in NN:
    if not any(min_<=n<=max_ for min_,max_ in FF):
        res+=n

print(res)

C = []
for n in N:
    add = True
    for nn in n:
        if not any(min_<=nn<=max_ for min_,max_ in FF):
            add = False
            break
    if add:
        C.append(n)

S = defaultdict(list)
for i in range(len(C[0])):
    D = []
    for j in range(len(C)):
        D.append(C[j][i])

    for name,f in F:
        fail = False
        for d in D:
            if not f[0][0]<=d<=f[0][1] and not f[1][0]<=d<=f[1][1]:
                fail = True
                break
        if not fail:
            S[name].append(i)

S = [(k,v) for (k,v) in S.items()]
R = dict()
while len(S):
    for s,v in S:
        if len(v)==1:
            R[s]=v[0]
            for ss,vv in S:
                if ss==s:
                    continue
                if v[0] in vv:
                    vv.remove(v[0])
            S.remove((s,v))
            break
res=1
for k,v in R.items():
    if k.startswith("departure"):
        res*=ticket[v]
print(res)
