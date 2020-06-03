# Sue 1: cars: 9, akitas: 3, goldfish: 0

S = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1
}

D = []

for line in open("16.in").readlines():
    line = line.strip()
    a, b = line.split(":", 1)
    a = int(a.split()[1])
    G = {}
    for bb in b.split(","):
        bb = bb.strip()
        k, v = [bbb.strip() for bbb in bb.split(":")]
        G[k] = int(v)
    D.append([a, G])


for n, d in D:
    correct = True
    for k in d.keys():
        if k == "cats" or k == "trees":
            if not (d[k] > S[k]):
                correct = False
                break    
        if k == "pomeranians" or k == "goldfish":
            if not (d[k] < S[k]):
                correct = False
                break    
        elif S[k] != d[k]:
            correct = False
            break
    if correct:
        print(n)
