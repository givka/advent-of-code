from collections import defaultdict

L = [l.strip() for l in open("04.in").readlines()]
id_count = 0

for line in L:
    D = defaultdict(int)

    for aa in line.split("-")[:-1]:
        for c in aa:
            D[c] += 1

    l = sorted(list(D.items()), key=lambda x: (-x[1], x[0]))
    l = "".join(ll[0]for ll in l)
    l = l[:5]

    line_id, b = line.split("-")[-1].split("[")
    line_id = int(line_id)
    b = b[:-1]

    if l == b:
        id_count += line_id


print(id_count)

for line in L:
    line_id, b = line.split("-")[-1].split("[")
    line_id = int(line_id)

    words = line.split("-")[:-1]

    def circle_letter(c, line_id):
        return chr((ord(c) - ord('a') + line_id) % 26 + ord('a'))

    translated = map(
        lambda word:  "".join(circle_letter(c, line_id) for c in word),
        words)

    translated = " ".join(translated)
    if translated == "northpole object storage":
        print(line_id)
