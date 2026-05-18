s = open("task24\\19489\\24_19489.txt").readline()

m = 0

for l in range(len(s)):
    for r in range(l + m, len(s)):
        c = s[l:r+1]
        if 'WSFWW' in c: break
        if c.count('WWF') > 120: break
        if c.count('WWF') <= 120 and 'WSFWW' not in c:
            m = max(m, len(c))
print(m)
# 3080