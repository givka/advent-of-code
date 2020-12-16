D = dict()

for line in open("07.in").readlines():
    line = line.strip()
    line = line.split("contain")
    bag_name = line[0].strip().split("bag")[0].strip()
    inside = [l.strip().split("bag")[0].strip()
              for l in line[1].strip().split(",")]
    if inside[0] == "no other":
        inside = []
    else:
        o = []
        for i in inside:
            i = i.split()
            assert(len(i) == 3)
            i = [int(i[0]), i[1]+" "+i[2]]
            o.append(i)
        inside = o
    D[bag_name] = inside


def get_goldies(color):
    if color == "shiny gold":
        return 1

    inside = D[color]

    if len(inside) == 0:
        return 0
    ans = 0
    for num, col in inside:
        ans += num * get_goldies(col)
    return ans


p1 = sum([get_goldies(key) > 0 for key in D if key != "shiny gold"])
print(p1)


def get_bags(color):
    inside = D[color]

    if len(inside) == 0:
        return 1

    ans = 0
    for num, col in inside:
        ans += num * get_bags(col)
        if len(D[col])!=0:
            ans+=num
    return ans


p2 = get_bags("shiny gold")
print(p2)
