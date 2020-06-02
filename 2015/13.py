from itertools import permutations
from collections import defaultdict

D = defaultdict(int)
S = set()

for line in open("13.in").readlines():
    line = line.strip()
    a, b = [l.strip() for l in line.split(
        "happiness units by sitting next to")]
    neighbour = b[:-1]
    person, count = [aa.strip() for aa in a.split("would")]
    sign, count = count.split()
    count = int(count)
    if sign == "lose":
        count *= -1
    S.add(person)
    D[person+"-"+neighbour] = count

S = list(S)

def happiness(S: list):
    P = permutations(S)
    R = []
    for p in P:
        c = 0
        for i in range(len(p)-1):
            c += D[p[i]+"-"+p[i+1]]
            c += D[p[i+1]+"-"+p[i]]
        c += D[p[-1]+"-"+p[0]]
        c += D[p[0]+"-"+p[-1]]
        R.append(c)
    return max(R)

print(happiness(S))

S.append("Me")
print(happiness(S))
