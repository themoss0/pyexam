c = 0
for l in open('9.25348.txt'):
    a = [int(x) for x in l.split()]
    p3 = [x for x in a if a.count(x) == 3]
    np = [x for x in a if a.count(x) == 1]
    pa = [x for x in a if a.count(x) > 1]
    maxa = max(a)
    if len(p3) == 3 and len(np) == 4 and (maxa not in pa):
        c += 1
print(c)
