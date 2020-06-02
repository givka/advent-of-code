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
    c = 0
    d = 0
    f = 0
    t = 0
    cal = 0
    for a in zip(i, I):
        c += a[0]*a[1][0]
        d += a[0]*a[1][1]
        f += a[0]*a[1][2]
        t += a[0]*a[1][3]
        cal += a[0]*a[1][4]
    if c < 0:
        c = 0
    if d < 0:
        d = 0
    if f < 0:
        f = 0
    if t < 0:
        t = 0
    R.append([c*d*f*t, cal])

print(max(R, key=lambda x: x[0])[0])
print(max([r for r in R if r[1] == 500], key=lambda x: x[0])[0])
