s = open("task24\\9169\\24_9169.txt").readline()

m = 10000

for l in range(len(s)):
    for r in range(l+m, l, -1):
        c = s[l:r+1]
        if c.count('BAD') < 3 and c.count('FAT') < 3: break
        if c.count('BAD') == 3 or c.count('FAT') == 3:
            m = min(m, len(c))
print(m)
# 10