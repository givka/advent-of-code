from collections import defaultdict

I = [11,18,0,20,1,7,16]

D = defaultdict(list)
last = None
turn = 1

for i in range(len(I)):
    last = I[i]
    D[last] = [turn]
    turn += 1

while turn <= 2020:
    if len(D[last])<2:
        last = 0
    elif len(D[last])==2:
        last = D[last][1]-D[last][0]

    D[last].append(turn)
    if len(D[last])==3:
        D[last] = D[last][1:]
    turn+=1

print(last)

D = defaultdict(list)
last = None
turn = 1

for i in range(len(I)):
    last = I[i]
    D[last] = [turn]
    turn += 1

while turn <= 30000000:
    if len(D[last])<2:
        last = 0
    elif len(D[last])==2:
        last = D[last][1]-D[last][0]

    D[last].append(turn)
    if len(D[last])==3:
        D[last] = D[last][1:]

    if turn % 1000000 == 0:
        print(turn, last)
    turn+=1

print(last)
