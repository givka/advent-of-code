from functools import reduce
I = []

for l in open("15.in").readlines():
    l = l.strip()
    l = l.replace(",", "")
    l = l.replace(":", "")
    name, _, capacity, _, durability, _, flavor, _, texture, _, calories = l.split()
    I.append([int(c)
              for c in [capacity, durability, flavor, texture, calories]])


def recursive(ii, s, out):
    if len(ii) == s:
        if sum(ii) == 100:
            # print(ii)
            out.append(ii)
            pass
        return
    for j in range(100-sum(ii)+1):
        jj = ii.copy()
        jj.append(j)
        recursive(jj, s, out)


out = []
for i in range(100+1):
    ii = [i]
    recursive(ii, len(I), out)

R = []
for i in out:
    ing = [0, 0, 0, 0, 0]
    for a, b in zip(i, I):
        ing[0] += a*b[0]
        ing[1] += a*b[1]
        ing[2] += a*b[2]
        ing[3] += a*b[3]
        ing[4] += a*b[4]
    ing = [max(ingg, 0) for ingg in ing]
    R.append([reduce(lambda x, y: x*y, ing[:-1]), ing[-1]])

print(max(R, key=lambda x: x[0])[0])
print(max([r for r in R if r[1] == 500], key=lambda x: x[0])[0])
