from ipaddress import *


def task13_23559_1():  # 718
    network = ip_network('102.162.200.51/255.255.255.0', 0)
    for i in network:
        print(i)
        print('--')


def task13_19245_2():  # 218.194.82.190 -> 21819482190
    network = ip_network('218.194.82.148/255.255.255.192', 0)
    for i in network:
        print(i)


def task13_MMigunov2026_3():  # 202.5.63.254-202.5.63.255
    network = ip_network('202.5.20.26/255.255.192.0', 0)
    for i in network:
        print(i)


def task13_23966_4():  # 172.47.255.254 -> 17247255254
    network = ip_network('172.45.129.10/255.240.0.0', 0)
    for i in network:
        print(i)


def task13_DBahtiev2026_5():  # 11
    for i in ip_network('150.122.11.21/255.255.254.0', 0):
        print(i)
        print(bin(150)[2:], bin(122)[2:], bin(10)[2:], bin(0)[2:])
        break


def task13_24063_6():  # 172111255254
    for i in ip_network('172.96.132.47/255.240.0.0', 0):
        print(i)


def task13_24231_7(): # 128
    for i in ip_network('116.192.155.16/255.255.255.0', 0):
        print(i)
    n1 = (bin(116)[2:])
    n2 = (bin(192)[2:])
    n3 = (bin(155)[2:])
    n = 0
    for i in range(2, 256):
        n4 = bin(i)[2:]
        if n4[-2] == n4[-1]:
            n += 1
    print(n)


def task13_24105_8(): # 12
    for i in ip_network('150.122.11.21/255.255.254.0', 0):
        print(i) # должно быть 150.122.10.1
        print((bin(150)[2:]+ bin(122)[2:]+ bin(10)[2:]+ bin(1)[2:]).count('1'))
        break


def task13_iglin_9():  # 202.71.127.254 -> 20271127254
    for i in ip_network('202.71.92.91/255.255.192.0', 0):
        x = bin(int(i))[2:]
        x1 = x[:8]
        x2 = x[8:16]
        x3 = x[16:24]
        x4 = x[24:32]
        if int(int(x1) % 2 != 0) + int(int(x2) % 2 != 0) + int(int(x3) % 2 != 0) + int(int(x4) % 2 != 0) == 2:
            print(i)


def task13_24047_10():
    for i in ip_network('23.78.143.87/255.255.240.0', 0):
        b = bin(int(i))[2:]
        b1 = b[0:8]
        b2 = b[8:16]
        b3 = b[16:24]
        b4 = b[24:32]
        r = [b1, b2, b3, b4]
        res = []
        for i in r:
            for s in i:
                c = 0
                if s != 1:
                    c += 1
                else:
                    res.append(c)
        if sum(res) > 6:
            print(i)
            break


def task13_24860_11():  # 1724515254
    for i in ip_network('172.45.12.200/255.255.240.0', 0):
        print(i)
task13_24860_11()