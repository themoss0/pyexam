def p(n):
    if n < 2: return False
    if n == 2: return True
    if n % 2 == 0: return False

    for d in range(3, int(n**0.5)+1, 2):
        if n % d == 0:
            return False
    return True

def d(n):
    if n == 0: return [0]
    i = 2
    dels = set()
    while n >= i * i:
        if n % i == 0:
            dels.add(i)
            dels.add(n//i)
        i+=1
    return list(dels)

c = 0
for n in range(1_474_999, 0, -1):
    if c != 5:
        
        dels = d(n)
        dels_p = [x for x in dels if p(x)]
        if dels_p:
            s = sum(dels_p)
        else:
            s = 0
        if s != 0 and s <= 42_000 and s % 6 == 0:
            print(n, s)
            c += 1
