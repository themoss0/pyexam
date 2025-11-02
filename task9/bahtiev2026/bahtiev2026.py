# ANSWER: 456865024

n = 1
for line in open('bahtiev2026.txt'):
    a = [int(x) for x in line.split()]
    p2 = [x for x in a if a.count(x) == 2]
    np = [x for x in a if a.count(x) == 1]
    mnp = min(np)
    if (len(p2) == 4 and len(np) == 3) and ((sum(p2) / len(p2)) <= mnp) and len(p2) > 0:
        print(a[0] * a[1] * a[2] * a[3] * a[4] * a[5] * a[6], n)
    n += 1