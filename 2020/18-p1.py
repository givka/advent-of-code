# for line in open("18.in"):
res = 0

lines = [
    "1 + 2 * 3 + 4 * 5 + 6",
    "1 + (2 * 3) + (4 * (5 + 6))",
    "5 + (8 * 3 + 9 + 3 * 4 * 3)",
    "5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))",
    "((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"
]

#lines = open)"18.in").readlines()

def process(line, idx=0):
    left = None
    op = None
    while idx < len(line):
        val = line[idx]
        print(idx, left, val)
        if val == "(":
            val,idxx = process(line, idx+1)
            idx += idxx-idx
        elif val == ")":
            return left,idx

        if not left:
            left = val
        elif not op:
            op = val
        else:
            left = left*val if op=="*" else left+val
            op = None
        idx += 1
    return left,idx

res = 0
for line in lines:
    L = []
    print(line)
    for char in line.split():
        for i in range(char.count("(")):
            L.append("(")

        n_char = char.replace("(","").replace(")","")
        L.append(int(n_char) if n_char.isdigit() else n_char)

        for i in range(char.count(")")):
            L.append(")")
    print(L)
    a,_ = process(L)
    print(a)
    res += a

print(res)


def process(line, idx=0):
    left = None
    op = None
    while idx < len(line):
        val = line[idx]
        #print(idx, left, val)
        if val == "(":
            val,idxx = process(line, idx+1)
            idx += idxx-idx
        elif val == ")":
            return left,idx


        if not left:
            left = val
        elif not op:
            op = val
        else:
            left = left*val if op=="*" else left+val
            op = None
        idx += 1
    return left,idx

print()

res = 0
for line in lines:
    L = []
    for char in line.split():
        for i in range(char.count("(")):
            L.append("(")

        n_char = char.replace("(","").replace(")","")
        L.append(int(n_char) if n_char.isdigit() else n_char)

        for i in range(char.count(")")):
            L.append(")")
    print("".join(str(l) for l in L))
    idx = 0
    LL = []
    level = 0
    levels = set()
    add = False
    b = "".join(str(l) for l in L)

    print(b.split("*"))

    while idx<len(L):
        val = L[idx]
        print(val, idx, level, levels)
        if val=="(":
            level += 1
        if val==")":
            level -= 1
            if level in levels:
                LL.append(")")
                levels.remove(level)

        if val == "+":
            last = LL[-1]
            LL.pop()
            LL.append("(")
            LL.append(last)
            add = True
        elif add:
            LL.append(")")
            add = False

        LL.append(val)
        idx += 1




    print("".join(str(l) for l in LL))
    print("")
    #a,_ = process(LL)
    #print(a)
    #res += a

#print(res)






