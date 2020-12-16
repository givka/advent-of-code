L = [int(l) for l in open("09.in").readlines()]

s = 25
idx = s
p1 = 0
for i in range(idx, len(L)):
    found = False
    for j in range(0, s+1):
        for k in range(j+1, s+1):
            if (L[i-j] + L[i-k]) == L[i]:
                found = True
                break
        if found:
            break
    if not found:
        p1 = L[i]
        break

print(p1)

ans = 0
idx = 0
idx2 = 0
while ans != p1:
    if ans > p1:
        idx += 1
        idx2 = idx
        ans = 0
    ans += L[idx2]
    idx2 += 1
print(min(L[idx:idx2])+max(L[idx:idx2]))
