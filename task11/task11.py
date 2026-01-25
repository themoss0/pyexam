from math import ceil


# this is my practise file of task number 8

def task11_23442_1():
    alphabet = 10 + 52 + 963
    c = 2000
    m = 693 * 1024 * 8
    l = m / c
    print(l)
    print({alphabet})
    print(l / 11)


def task11_21410_2():
    l = 257
    c = 295_740
    mem = 33 * 1024 * 1024 * 8
    p = l * c
    res1 = mem // p
    print(res1)


def task11_23557_3():  # 896
    a = 500 + 52 + 10
    i = 10
    c = 45_877
    mem = 49 * 1024 * 1024 * 8
    print(ceil(mem / c / i))


def task11_19243_4():  # 5.19 -> 6 -> 2^6 = 64(min = 33)
    l = 377
    c = 23_155
    mem = 5536 * 1024 * 8
    print((mem // c) / 377)


def task11_MMigunov2026_5():  # 8
    a = 31
    i = 5
    c = 7_654_321
    mem = 36 * 1024 * 1024 * 8
    for n in range(1, 100):
        if mem <= c * i * n:
            print(n, mem - c * i * n)
    print('----')
    print(mem - c * i * 7)
    print(mem - c * i * 8)


def task11_23964_6():  # 8193
    l = 12
    c = 200_000
    mem = 4 * 1024 * 1024 * 8
    for i in range(1, 20):
        if mem >= c * l * i:
            print(i)
    print(2 ** 13 + 1)


def task11_LShastin2026_7():  # 53819
    a = 10 + 52 + 454
    i = 10
    c = 31_922
    mem = 2 * 1024 * 1024 * 1024 * 8
    for x in range(100000, 1, -1):
        if i * c * x > mem:
            print(x)


def task11_24062_8():  # 9 -> 2**9 == 256 -> 256+1 = 257
    l = 3425
    c = 2_718_281
    mem = 9 * 1024 * 1024 * 1024 * 8
    for i in range(1, 20):
        if mem <= l * i * c:
            print(f'{i=}, mem={i * c * l}, {mem <= l * i * c}')
            break


def task11_24229_9():  # 8193
    l = 120
    c = 50_000
    mem = 10 * 1024 * 1024
    for i in range(1, 20):
        if mem <= c * l * i // 8:
            print(i, 2 ** i + 1)
            print(mem <= 13 * c * l)


def task11_24072_10():  # 53818
    a = 10 + 52 + 454
    i = 10
    c = 31_922
    membit = 2 * 1024 * 1024 * 1024 * 8
    xbyte = ceil((c * i) / 8)
    for i in range(0, 60000):
        if xbyte * i > membit / 8:
            print(i)
            break


def task11_24858_11():
    l = 150
    c = 50_000
    mem = 12 * 1024 * 1024 * 8

    for i in range(1, 40):
        if mem / 8 >= (l * i * c) / 8:
            print(i, mem / 8 >= (l * i * c) / 8)
            print(2 ** i + 1)


def task11_25350_12():  # 257
    l = 105
    c = 65_536
    mem = 7 * 1024 * 1024 * 8
    for i in range(0, 30):
        if (l * i * c) / 8  <= mem / 8:
            print(i, 2**i+1)
task11_25350_12()