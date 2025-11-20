def p(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def d(n):
    i = 2
    R = set()
    while i * i < n:
        if n % i == 0:
            if p(i):
                n //= i
                R.add(i)
        i += 1
        if len(R) == 12:
            return list(R)
    return []


c = 0
for n in range(24_517_512, 100_000_000):
    l = d(n)
    if len(l) == 12:
        print(n, max(n))
        c += 1
    if c == 5:
        break
