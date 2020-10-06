import hashlib

base = "reyedfim"
i = 0
password = ""
while(True):
    code = base + str(i)
    code = hashlib.md5(code.encode()).hexdigest()
    if code.startswith("00000"):
        password += code[5]
        print(len(password), password)
        if len(password) == 8:
            break
    i += 1

print(password)

base = "reyedfim"
i = 0
password = " ".join("" for c in range(8))
D = set()
while(True):
    code = base + str(i)
    code = hashlib.md5(code.encode()).hexdigest()

    if code.startswith("00000") and code[5].isdigit() and int(code[5]) not in D and 0 <= int(code[5]) < 8:
        index = int(code[5])
        D.add(index)
        password = password[:index] + code[6] + password[index + 1:]
        print(len(D), password)
        if len(D) == 8:
            break
    i += 1

print(password)
