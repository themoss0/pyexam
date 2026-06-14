# ANSWER: 901

num = []
i = 1
for line in open('task9/23747/23747.txt'):
    a = [int(x) for x in line.split()]
    p3 = [x for x in a if a.count(x) == 3]
    np = [x for x in a if a.count(x) == 1]
    if len(p3) > 0 and len(np) != 0 and sum(np) / len(np) <= p3[0]:
        num.append((i, a, sum(a)))
    i+=1
print(num[-1])