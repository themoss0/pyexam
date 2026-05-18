s = open('task24\\26549\\24_26549.txt').readline()

m = 0

for l in range(len(s)):
    for r in range(l + m, len(s)):
        c = s[l:r+1]
        if c.count('2025') > 50: break
        if c[-4:] == '2025' and c.count('Y') >= 140 and c.count('2025') == 50:
            m = max(m, len(c))
print(m) 
# 938