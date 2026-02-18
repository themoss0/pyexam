# Task 23565

def f(s, m):
	if (s <= 15):
		return m%2==0
	if(m == 0):
		return 0
	h = [
		f(s-3, m-1),
		f(s-8, m-1),
		f(s//3, m-1)
	]
	return any(h) if m%2!=0 else all(h)


print(min([x for x in range(16, 100) if f(x, 2)]))
print([x for x in range(16, 100) if not f(x, 1) and f(x, 3)][:2])
print(min([x for x in range(16, 100) if not f(x, 2) and f(x, 4)]))