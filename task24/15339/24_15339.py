s = open("task24\\15339\\24_15339.txt").readline()

for x in '789': s = s.replace(x, '6')
for x in "BC": s = s.replace(x, 'A') 

m = 0

for l in range(len(s)):
    for r in range(l+m, len(s)):
        c = s[l:r+1]
        if 'AA' in c: break
        if '66' in c: break
        if 'AA' not in c and '66' not in c:
            m = max(m, len(c))
print(m)
# 22