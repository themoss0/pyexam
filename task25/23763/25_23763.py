'''
800004 400004
800009 114294
800013 266674
800024 400014
800033 61554
'''

def ds(n):
    dels = set()
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            dels.add(i)
            dels.add(n//i)
    dels = sorted(dels)
    if len(dels) > 1:
        return dels[0] + dels[-1]
    return 0

c = 0
for n in range(800_001, 1_000_000):
    if c != 5:
        m = ds(n)
        if m % 10 == 4:
            print(n, m)
            c += 1