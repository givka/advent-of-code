import hashlib

P = open("04.in").read().strip()

p = ""
i = 0
while not p.startswith("000000"):
    i += 1
    a = hashlib.md5()
    a.update((P + str(i)).encode('utf-8'))
    p = a.hexdigest()

print(i)