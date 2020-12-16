L = [line.strip() for line in open("13.0").readlines()]

timestamp = int(L[0])
ids = L[1].split(",")
m = 1<<100
res = 0
for id_ in ids:
    if id_ == "x":
        continue
    id_ = int(id_)
    if m > id_-(timestamp%id_):
        m = id_-(timestamp%id_)
        res = m*id_
print(res)

ids = [1789,37,47,1889]
ids = [(i,int(id_)) for i,id_ in enumerate(ids) if id_ != "x"]
print(ids)

num = 0
while True:
    found = True
    for i,ii in ids:
        if (num+i)%ii!=0:
            found = False
            break
        if not found:
            break
    if found:
        print(num)
        break
    num+=1
#The earliest timestamp that matches the list 17,x,13,19 is 3417.
#67,7,59,61 first occurs at timestamp 754018.
#67,x,7,59,61 first occurs at timestamp 779210.
#67,7,x,59,61 first occurs at timestamp 1261476.
#1789,37,47,1889 first occurs at timestamp 1202161486.

