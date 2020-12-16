def slope(L, right,down):
    w = len(L[0])
    x,y = 0,0
    occ = 0
    while y < len(L)-1:
        x+=right
        y+=down
        if L[y][x%w]=="#":
            occ+=1
    return occ

L = [line.strip() for line in open("03.in").readlines()]
print(slope(L,3,1))
print(slope(L,1,1)*slope(L,3,1)*slope(L,5,1)*slope(L,7,1)*slope(L,1,2))