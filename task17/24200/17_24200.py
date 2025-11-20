# ANSWER: 3 86323

with open('17_24200.txt') as file:
    data = [int(x) for x in file.readlines()]
c = 0
max_a = -50000000
kolvo_ch = len([x for x in data if x % 2 == 0])

def ch(n1, n2):
    return (len(str(n1)) > 2 and len(str(n2)) > 2) and int(str(n1)[-3] == '0') + int(str(n2)[-3] == '0') >= 1

for i in range(0, len(data)-1):
    if ch(data[i], data[i+1]) and (int(data[i]) * int(data[i+1])) % kolvo_ch == 0:
        c += 1
        max_a = abs(max(max_a, int(data[i]) + int(data[i+1])))
print(c, max_a)