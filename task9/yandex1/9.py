n = 1
for line in open('9.txt'):
	a = [int(x) for x in line.split()]
	p2 = [x for x in a if a.count(x) == 2]
	u1 = len(p2) == 4
	u2 = max(a) not in p2
	if u1 and u2:
		print(n)
	n += 1
