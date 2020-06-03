from itertools import combinations

N = [int(l.strip()) for l in open("17.in").readlines()]
NN = 150

id = 0
M = []
for n in N:
    M.append(tuple([n, id]))
    id += 1

S = set()
for i in range(len(M)):
    print(i+1)
    for l in list(combinations(M, i+1)):
        if sum(map(lambda x: x[0], l)) == NN:
            S.add(l)

print(len(S))

S = list(S)
a = min(list(S), key=lambda x: len(x))
b = filter(lambda x: len(x) == len(a), list(S))
print(len(list(b)))