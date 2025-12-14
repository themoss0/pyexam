# ANSWER: 1020 72079

with open('17_20342.txt') as file:
    data = [int(x) for x in file.readlines()]


mx = max([x for x in data if abs(x) % 100 == 42])
c = 0
ms = -100000000

def ch(n1, n2):
    return int(abs(n1) % 100 == 42 and 9999 < abs(n1) < 100_000)\
+ int(abs(n2) % 100 == 42 and 9999 < abs(n2) < 100_000) == 1

for i in range(0, len(data)-1):
    if ch(data[i], data[i+1]) and (data[i] ** 2 + data[i+1] ** 2 >= mx ** 2):
        c += 1
        ms = max(ms, data[i] + data[i+1])
print(c, ms)