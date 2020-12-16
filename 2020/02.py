L = []
for line in open("02.in").readlines():
    line = line.strip()
    occ, letter, password = line.split()
    occ =  list(map(int, occ.split("-")))
    letter = letter[0]
    L.append((occ,letter,password))

res = 0
for occ,letter,password in L:
    if occ[0]<=password.count(letter)<=occ[1]:
        print(occ,letter,password)
        res+=1
print(res)

res = 0
for occ,letter,password in L:
    a = password[occ[0]-1]==letter
    b = password[occ[1]-1]==letter
    if (a and not b) or (not a and b):
        print(occ,letter,password)
        res+=1
print(res)