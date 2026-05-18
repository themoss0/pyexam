s = open("task24\\14510\\24_14510.txt").readline()

for x in 'EIOUY': s = s.replace(x, 'A')
for x in 'CDFGHIJKQLMNPRSTVWXZ': s = s.replace(x, 'B')

m = 10000

for l in range(len(s)):
    for r in range(l+m, l, -1):
        c = s[l:r+1]
        if c.count('BBA') < 500: break
        if c.count('BBA') >= 500:
            m = min(m, len(c))
print(m)
# 3493