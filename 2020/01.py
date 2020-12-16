L = [int(line) for line in open("01.in").readlines()]

for i in range(len(L)):
    for j in range(len(L)):
        for k in range(len(L)):
            if i==j==k:
                continue
            if L[i]+L[j]+L[k]==2020:
                print(L[i]*L[j]*L[k])
                exit(0)
