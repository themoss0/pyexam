# ANSWER: 3309

c = 0
for line in open('21497.txt'):
    a = [int(x) for x in line.split()]
    np = [x for x in a if a.count(x) == 1]
    max2 = sorted(a)[-2:]
    sp4 = sorted(a)[0:4]
    f1 = len(np) == 6
    f2 = (2 * sum(max2)) >= (3 * sum(sp4))
    if f1 and f2:
        c += 1
        print(a, sorted(np), max2, sp4, sep='\n')
print(c)