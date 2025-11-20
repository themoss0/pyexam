# ANSWER: 149

c = 0
for line in open('23809.txt'):
    a = [int(x) for x in line.split()]
    p2 = [x for x in a if a.count(x) == 2]
    p2s = set(p2)
    np = [x for x in a if a.count(x) == 1]
    nps = set(np)
    f1 = len(p2s) == 3 and len(nps) == 1
    f2 = len(p2s) != 0 and len(np) != 0 and sum(p2s) / len(p2s) >= np[0]
    if f1 and f2:
        c += 1
print(c)
