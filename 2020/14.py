L=[l.strip() for l in open("14.in").readlines()]

cur = []
mask = None
M= []
for l in L:
    if l[0:4]=="mask":
        if mask:
            M.append((mask,cur))
        l = l.split("=")
        mask = l[1].strip()
        cur = []
    else:
        a,b = l.split("=")
        a = a.split("[")
        a = int(a[1].split("]")[0])
        b = bin(int(b.strip()))[2:]
        cur.append((a,b))

if mask:
    M.append((mask,cur))

ans=0
d = {}
for mask,cur in M:
    for mem,val in cur:
        val = val.zfill(36)
        res = ""
        for i in range(36):
            res+=mask[i] if mask[i]!="X" else val[i]
        d[mem]=int(res,2)
for k,v in d.items():
    ans+=v
print(ans)
print()

ans=0
d = {}
for mask,cur in M:
    for mem,val in cur:
        mem = bin(int(mem))[2:]
        mem = mem.zfill(36)
        add = ""
        for i in range(36):
            add+=mem[i] if mask[i]=="0" else mask[i]
        n = add.count("X")
        for i in range(2**n):
            add2 = add
            b = bin(i)[2:].zfill(n)
            for j in range(n):
                add2 = add2.replace("X",b[j], 1)
            d[int(add2,2)]=int(val,2)
for k,v in d.items():
    ans+=v
print(ans)
