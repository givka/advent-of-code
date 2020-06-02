S = open("12.in").readline().strip()

R = []
for i in range(len(S)):
    if S[i:i + 3] == "red":
        mmin = i - 1
        level = 0
        if S[i - 2] != ":":
            continue
        while True:
            if S[mmin] == "}":
                level += 1
            if S[mmin] == "{":
                level -= 1
                if level == -1:
                    break
            mmin -= 1
        mmax = i
        level = 0
        while True:
            if S[mmax] == "}":
                level += 1
                if level == 1:
                    break
            if S[mmax] == "{":
                level -= 1
            mmax += 1
        R.append(S[mmin:mmax + 1])

print(len(S))
for r in R:
	S = S.replace(r, "")
print(len(S))

S = S.replace("[", "")
S = S.replace("]", "")
S = S.replace("{", "")
S = S.replace("}", "")
S = S.replace("\"", "")
S = S.replace(":", "")

for i in range(ord("a"), ord("z") + 1):
    S = S.replace(chr(i), "")

S = [int(s.strip()) for s in S.split(",") if s != ""]
print(sum(S))
