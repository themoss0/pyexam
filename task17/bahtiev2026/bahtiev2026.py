# ANSWER: 23 20600

with open('17.txt') as file:
    data = [int(x) for x in file.readlines()]

c = 0
ms = -30001
mpe = min([x for x in data if 99 < x < 1000])

def ch(n1, n2, n3):
    return int(99 < abs(n1) < 1000) + int(99 < abs(n2) < 1000) + int(99 < abs(n3) < 1000) == 1

for i in range(len(data)-2):
    if ch(data[i], data[i+1], data[i+2]) and ((int(data[i]) + int(data[i+1]) + int(data[i+2])) % mpe == 0):
        c += 1
        ms = max(ms, (int(data[i]) + int(data[i+1]) + int(data[i+2])))
print(c, ms)