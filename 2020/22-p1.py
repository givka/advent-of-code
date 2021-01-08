from collections import deque

L = [line.strip() for line in open("22.in").readlines()]

p1 = deque()
p2 = deque()
player = p1

for line in L:
    if not line:
        player = p2
    elif not line.startswith("Player"):
        player.append(int(line))

while len(p1) and len(p2):
    c1, c2 = p1.popleft(), p2.popleft()
    if c1 > c2:
        p1.append(c1)
        p1.append(c2)
    else:
        p2.append(c2)
        p2.append(c1)

player = p1 if len(p1) else p2
ans = 0
for i, c in enumerate(player):
    ans += (len(player)-i)*c
print(ans)
