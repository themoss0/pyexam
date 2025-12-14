'''
ANSWER:
1000020 2201387
1000054 653641
1000056 1500143
1000066 532093
1000078 504289
'''

def d(n):
    res = set()
    i = 2
    while i * i <= n:
        if n % i == 0:
            res.add(i)
            res.add(n // i)
        i += 1
    return sorted(res)

def p(n):
    i = 2
    if n == 0:
        return False
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True
c = 0
for n in range(1_000_000, 2_000_000):
    q = sum(d(n))
    if p(q):
        print(n, q)
        c += 1
    if c == 5:
        break
