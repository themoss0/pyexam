s = open("task24\\28765_dosrok_2026\\24_28765.txt").readline()

c = ''
k = 0
m = 0

for r in range(len(s)):
    c += s[r]
    if c[-2:] == 'BC': k += 1
    while k > 180:
        if c[:2] == 'BC': k -= 1
        c = c[1:]
    m = max(m, len(c))
    if r%100_000==0: print(r, len(c), m)
print(m)