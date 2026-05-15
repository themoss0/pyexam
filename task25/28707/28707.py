from math import log, sqrt

c = 0
for n in range(8_699_999, 1, -1):
	if ('1' in str(n) or '3' in str(n)):
		for i in range(1, 9):
			pow7 = 7 ** i
			if pow7 >= n:
				break
			rem = n - pow7
			if rem % 2 != 0:
				continue
			root = int(sqrt(rem))
			if root * root == rem and root % 2 == 0:
				print(n, i)
				c += 1
		if (c == 5):
			break
