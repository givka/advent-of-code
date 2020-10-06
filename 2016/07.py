lines = [l.strip() for l in open("07.in").readlines()]

def check_abba(word: str):
    for i in range(len(word)-3):
        if (word[i] == word[i+3] and word[i+1] == word[i+2] and word[i] != word[i+1]):
            return True
    return False


count = 0
for line in lines:
    insides = []
    outsides = []
    words = line.split("[")
    for w in words:
        pairs = w.split("]")
        if len(pairs) == 2:
            insides.append(pairs[0])
            outsides.append(pairs[1])
        else:
            outsides.append(w)

    if not any(check_abba(x)for x in insides) and any(check_abba(x) for x in outsides):
        count += 1
print(count)


def check_aba(word: str):
    res = []
    for i in range(len(word)-2):
        if (word[i] == word[i+2] and word[i] != word[i+1]):
            res.append(word[i:i+3])
    return res


count = 0
for line in lines:
    insides = []
    outsides = []
    words = line.split("[")
    for w in words:
        pairs = w.split("]")
        if len(pairs) == 2:
            insides.append(pairs[0])
            outsides.append(pairs[1])
        else:
            outsides.append(w)

    out_aba = []
    for o in outsides:
        out_aba.extend(check_aba(o))

    in_aba = []
    for i in insides:
        in_aba.extend(check_aba(i))

    found = False
    for o in out_aba:
        for i in in_aba:
            if o[1]+o[0]+o[1] == i:
                count += 1
                found = True
                break
        if found:
            break


print(count)
