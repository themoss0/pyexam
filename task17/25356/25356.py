# ANSWER: 1032 285423

with open('17_25356.txt') as file:
    data = [int(x) for x in file.readlines()]

max30 = max([x for x in data if x % 100 == 30])
c = 0
ms = -100000000000

def ch(n1, n2, n3) -> bool:
    return int(999 < abs(int(n1)) < 10000) + int(999 < abs(int(n2)) < 10000) \
+ int(999 < abs(int(n3)) < 10000) == 0

for i in range(0, len(data)-2):
    if int(data[i]) + int(data[i+1]) + int(data[i+2]) > max30 and ch(int(data[i]), int(data[i+1]), int(data[i+2])):
        c += 1
        ms = max(ms, int(data[i]) + int(data[i+1]) + int(data[i+2]))
print(c, ms)