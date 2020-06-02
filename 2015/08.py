import re

W = [l.strip() for l in open("08.in").readlines()]

count = 0
real = 0

def is_hex(s):
    try:
        int(s, 16)
        return True
    except ValueError:
        return False

for w in W:
    print(w)
    real += len(w)
    w = w.replace("\\\"", "\"").replace("\\\\", "\\")
    count += len(w) - 2
    i=0
    c = 0
    while i<len(w):
        if i<len(w)-4 and w[i]=="\\" and w[i+1]=="x"and is_hex(w[i+2]+w[i+3]):
            i+=4
            c+=1
        i+=1
    count-=c*3


print(real, count, real - count)
