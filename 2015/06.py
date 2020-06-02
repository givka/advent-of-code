#turn off 199,133 through 461,193
#toggle 322,558 through 977,958
#turn on 226,196 through 599,390

M = [[0 for j in range(0,1000)] for i in range(0,1000)]
C = []
for line in open("06.in").readlines():
    line  = line.strip()
    begin, end = [l.strip() for l in line.split("through")]
    begin = begin.split()
    end = [int(x) for x in end.split(",")]
    if len(begin)==3:
        begin = [" ".join(begin[:2]),begin[2]]
    instr, begin = begin[0], [int(x) for x in  begin[1].split(",")]
    C.append([instr,begin,end])


for instr,begin,end in C:
    for r in range(begin[1], end[1]+1):
        for c in range(begin[0], end[0]+1):
            if instr=="turn on":
                M[r][c]=1
            elif instr == "turn off":
                M[r][c]=0
            else:
                M[r][c]=not M[r][c]

count = 0
for r in range(len(M)):
    for c in range(len(M[0])):
        if M[r][c] == 1:
            count+=1
print(count)

M = [[0 for j in range(0,1000)] for i in range(0,1000)]

for instr,begin,end in C:
    for r in range(begin[1], end[1]+1):
        for c in range(begin[0], end[0]+1):
            if instr=="turn on":
                M[r][c] += 1
            elif instr == "turn off":
                M[r][c] = max(M[r][c]-1, 0)
            elif instr == "toggle":
                M[r][c] += 2

count = 0
for r in range(len(M)):
    for c in range(len(M[0])):
        count+=M[r][c]
print(count)


