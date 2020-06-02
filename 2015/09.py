# London to Dublin = 464
# London to Belfast = 518
# Dublin to Belfast = 141
from itertools import permutations

M = {}
S = set()
for l in open("09.in").readlines():
    l = l.strip()
    a, d = [ll.strip() for ll in l.split("=")]
    f, t = [aa.strip() for aa in a.split("to")]
    S.add(f)
    S.add(t)
    M[f + "-" + t] = int(d)
    M[t + "-" + f] = int(d)


S = list(S)
travels = list(permutations(S))

D = []
for t in travels:
	d = 0
	for i in range(len(t)-1):
		d+=M[t[i]+"-"+t[i+1]]
	D.append(d)

print(min(D))
print(max(D))