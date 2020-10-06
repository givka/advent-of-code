T = []

for l in open("03.in").readlines():
    l = l.strip().split()
    T.append(list(map(int, l)))

count = 0
for t in T:
    nums = sorted(t)
    if nums[0]+nums[1] > nums[2]:
        count += 1

print(count)

count = 0
for t in range(0, len(T), 3):
    for i in range(3):
        nums = sorted([T[t][i], T[t+1][i], T[t+2][i]])
        if nums[0]+nums[1] > nums[2]:
            count += 1
print(count)