'''
ANSWER:
1350051 311
1350055 270011
1350062 511
1350063 40911
1350066 225011
'''



def d(n):
    dels = set()
    i = 1
    while i * i <= n:
        if (n % i == 0):
            dels.add(i)
            dels.add(n // i)
        i += 1
    return sorted(dels)
c = 0
for n in range(1_350_050, 1_500_000):
    dels = [x for x in d(n) if x % 100 == 11 and x != n and x != 11]
    if len(dels) > 0:
        print(n, min(dels))
        c += 1
    if c == 5:
        break
