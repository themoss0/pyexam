# 2981

s = open('task24\\23762\\24_23762.txt').readline()

m = 0

for l in range(len(s)):
    for r in range(l+m+1, len(s)):
        c = s[l:r]
        if c.count('Y') > 80: break
        if c.count('Y') == 80 and c.count('2025') >= 90:
            m = max(m, len(c))
            
print(m)