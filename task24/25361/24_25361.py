s = open('task24\\25361\\24_25361.txt').readline()

m = 0

for l in range(len(s)):
    for r in range(l+m, len(s)):
        c = s[l:r+1]
        if c.count('F') > 76: break
        if c[0] not in '02468': break
        if len([x for x in c if x in '02468']) > 1: break
        if c.count('F') == 76 and c[0] in '02468' and len([x for x in c if x in '02468']) == 1:
            m = max(m, len(c))
print(m)
# 163