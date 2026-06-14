# 150 9930

with open('task17\\23757\\17_23757.txt') as file:
    data = [int(x) for x in file.readlines()]

min2 = min([x for x in data if 10 <= x <= 99])
c = 0
ms = -1000000

def ch(n1, n2):
    return int(10 <= n1 <= 99) + int(10 <= n2 <= 99) == 1

for i in range(len(data)-1):
    if ch(data[i], data[i+1]) and (data[i] + data[i+1]) % min2 == 0:
        c += 1
        ms = max(ms, data[i]+data[i+1])
print(c, ms)
