from collections import defaultdict

lines = [l.strip() for l in open('06.in').readlines()]

pswd = ""
for i in range(len(lines[0])):
    D = defaultdict(int)
    for line in lines:
        D[line[i]] += 1
    pswd += max(D.items(), key=lambda x: x[1])[0]
print(pswd)

pswd = ""
for i in range(len(lines[0])):
    D = defaultdict(int)
    for line in lines:
        D[line[i]] += 1
    pswd += min(D.items(), key=lambda x: x[1])[0]
print(pswd)