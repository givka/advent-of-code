T = open('01.in').readline()
opened = T.count('(')
closed = T.count(')')
print(opened - closed)

level = 0
pos = 1
for c in T:
    if c == '(':
        level += 1
    else:
        level -= 1
    if level == -1:
        print(pos)
        break
    pos += 1
