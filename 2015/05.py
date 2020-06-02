S = [l.strip() for l in open("05.in").readlines()]
F = ["ab", "cd", "pq", "xy"]
A = [i for i in range(ord("a"), ord("z")+ 1)]

count=0
for s in S:
    if any(s.count(f) != 0 for f in F):
        continue
    if not any([s.count(chr(a)+chr(a))for a in A]):
        continue
    if sum([s.count(c) for c in "aeiou"])<3:
        continue
    count+=1

print(count)

count=0
good = False
for s in S:
    for i in range(len(s)-1):
        if good:
            break
        for j in range(i+1, len(s)):
            if s.count(s[i]+s[j]) > 1:
                good=True
                break
    if not good:
        continue

    if not any([s.count(chr(a)+chr(b)+chr(a))for a in A for b in A]):
        good = False

    if good:
        count +=1

print(count)

