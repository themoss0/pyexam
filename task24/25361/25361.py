with open('24_25361.txt') as file:
    data_list = [x for x in file.readlines()]

data = ''
for i in data_list:
    data += i
#print(data)
row = ''
for i in range(0, len(data) - 1):
    for j in range(0, len(data) - 1):
        if data[j].isdigit() and int(data[j]) % 2 == 0:
            row += data[j]
            while (not data[j].isdigit()) and (int(data[j]) % 2 != 0):
                row += data[j]
    if row.count('F') == 76:
        print(len(row))