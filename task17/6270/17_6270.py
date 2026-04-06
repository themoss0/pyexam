with open('task17/6270/17_6270.txt') as file:
    data = [int(x) for x in file.readlines()]

c = 0

pairs = []
kdrz = []

def ch(n1, n2):
    return int(abs(n1) % 10 == 7) + int(abs(n2) % 10 == 7) == 1


for i in range(0, len(data)-1):
    if ch(data[i], data[i+1]):
        pairs.append([data[i], data[i+1]])
        kdrz.append((data[i]-data[i+1])**2)

if kdrz:
    m = max(abs(x1*x1 - x2*x2) for x1, x2 in pairs)
else:
    m = 0

res = []
for i in range(len(pairs)):
    x1, x2 = pairs[i]
    d = x1 - x2
    s = d * d
    if (s < m):
        res.append(s)
print(len(res), min(res))