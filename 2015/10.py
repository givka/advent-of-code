I = "3113322113"

for j in range(50):
	c = None
	cnt = 0
	res = ""

	for i in I:
		if c is None:
			c = i
		if c == i:
			cnt+=1
		else:
			res += str(cnt)+c
			c = i
			cnt=1
	res += str(cnt)+i
	I = res

print(len(I))