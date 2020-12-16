import math

L = [int(l.strip()) for l in open("10.1").readlines()]

L.append(0)
L.append(max(L)+3)
L = sorted(L)

print(L)

ones = 0
threes = 0
G = []
for i in range(len(L)-1):
    val = L[i+1]-L[i]
    if val == 1:
        ones += 1
    else:
        threes += 1
    G.append(val)

print()
print(ones * threes)
print()


def f(n, k):
    return math.factorial(n)/(math.factorial(k)*math.factorial(n-k))


# Q = []
# for i in range(len(G)-2):

#     v1 = G[i] == 1 and G[i+1] == 1
#     v2 = G[i] == 1 and G[i+1] == 1 and G[i+2] == 1
#     Q.append(v1)
#     Q.append(v2)

# Q = list(reversed(Q))
# print(Q)

# last = 0
# idx = 0
# M = []
# print()
# while idx < len(Q):
#     occ = 0
#     l_i = idx
#     while idx < len(Q) and Q[idx]:
#         idx += 1
#         occ += 1

#     if occ:
#         M.append(occ)
#     idx += 1


# print(M)

# res = 1
# for m in M:
#     res *= m*2
# print(res)

i = 0
while i < len(G):
    while i < len(G) and L[i+1]-L[i] == 1 and L[i+2]-L[i] <= 3:
        print("lol")
        i += 1
    print("-"*10)
    i += 1
