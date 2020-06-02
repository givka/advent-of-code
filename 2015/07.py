D = {}
SEEN = {}
for line in open("07.in").readlines():
    line = line.strip()
    prod, res = [c.strip() for c in line.split("->")]
    D[res] = prod

def process(key: str):
    if key in SEEN:
        return SEEN[key]
    if key.isdigit():
        return int(key)
    prod, res = D[key].split(), key
    if len(prod)==1:
        SEEN[key] = process(prod[0])
    if len(prod)==2:
        SEEN[key] =  ~ process(prod[1])
    if len(prod)==3:
        a,cmd,b = prod
        if cmd == "OR":
            SEEN[key] = process(a) | process(b)
        if cmd == "AND":
            SEEN[key] = process(a) & process(b)
        if cmd == "LSHIFT":
            SEEN[key] = process(a) << process(b)
        if cmd == "RSHIFT":
            SEEN[key] = process(a) >> process(b)
    if SEEN[key]<0:
        SEEN[key] += 65535+1
    print(key, SEEN[key])

    return SEEN[key]

result = process("a")
print(result)

D = {}
SEEN = {}
for line in open("07.in").readlines():
    line = line.strip()
    prod, res = [c.strip() for c in line.split("->")]
    D[res] = prod

D["b"] = str(result)

result = process("a")
print(result)



