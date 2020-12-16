import pprint

L = [line.strip() for line in open("04.in").readlines()]
K = [
    "byr",
    "iyr",
    "eyr",
    "hgt",
    "hcl",
    "ecl",
    "pid",
    "cid",
]

P = []
cur = []
ans = 0
for line in L:
    if line == "":
        P.append(cur)
        cur = []
    else:
        cur.extend(line.split())
P.append(cur)

for cur in P:
    d = dict()
    for c in cur:
        k, v = c.split(":")
        d[k] = v
    add = 1

    for k in K:
        if k not in d:
            if k != "cid":
                add = 0
    ans += add

print(ans)


# byr (Birth Year) - four digits; at least 1920 and at most 2002.
# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
# hgt (Height) - a number followed by either cm or in:
# If cm, the number must be at least 150 and at most 193.
# If in, the number must be at least 59 and at most 76.
# cid (Country ID) - ignored, missing or not.

ans = 0
for cur in P:
    d = dict()
    for c in cur:
        k, v = c.split(":")
        d[k] = v
    add = 1

    for k in K:
        if k not in d:
            if k != "cid":
                add = 0
    if add == 0:
        continue

    if not (d["byr"].isdigit() and 1920 <= int(d["byr"]) <= 2002):
        continue
    print(d["byr"])

    if not (d["iyr"].isdigit() and 2010 <= int(d["iyr"]) <= 2020):
        continue
    print(d["iyr"])

    if not (d["eyr"].isdigit() and 2020 <= int(d["eyr"]) <= 2030):
        continue
    print(d["eyr"])

    if not ((d["hgt"][-2:] == "cm" and d["hgt"][:-2].isdigit() and 150 <= int(d["hgt"][:-2]) <= 193) or
            (d["hgt"][-2:] == "in" and d["hgt"][:-2].isdigit() and 59 <= int(d["hgt"][:-2]) <= 76)):
        continue
    print(d["hgt"])

    # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    if not(d["hcl"][0] == "#" and len(d["hcl"]) == 7 and all(['0' <= c <= '9' or 'a' <= c <= 'f' for c in d["hcl"][1:]])):
        continue
    print(d["hcl"])

    # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    if not(d["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]):
        continue
    print(d["ecl"])

    # pid (Passport ID) - a nine-digit number, including leading zeroes.
    if not(d["pid"].isdigit() and len(d["pid"]) == 9):
        continue
    print(d["pid"])

    print()

    ans += add

print(ans)
