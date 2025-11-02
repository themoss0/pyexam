from string import printable
from sys import set_int_max_str_digits

set_int_max_str_digits(10000)


def sys(s: int, c: int) -> str:
    res = ''
    while s > 0:
        res = str(s % c) + res
        s //= c
    return res


def task14_20284_1():
    for x in range(0, 42):
        a = 19 * 42 ** 4 + 5 * 42 ** 3 + 6 * 42 ** 2 + 9 * 42 ** 1 + x * 42 ** 0
        a += 1 * 42 ** 3 + x * 42 ** 2 + 18 * 42 ** 1 + 10 * 42 ** 0
        if a % 155 == 0:
            print(x, a // 155)


def task14_21413_2():
    for x in printable[:21]:
        a = int(f'82934{x}2', 21) + int(f'2924{x}{x}7', 21) + int(f'67564{x}8', 21)
        if a % 20 == 0:
            print(x, a // 20)


def task14_23560_3():
    for x in range(1, 2401):  # 2394
        n = 7 * 9 ** 210 + 6 * 9 ** 110 - x
        if sys(n, 9).count('0') == 100:
            print(x, sys(n, 9).count('0'))


def task14_23560_3():  # 266249847
    for x in printable[:25]:
        a = int(f'11353{x}12', 25) + int(f'135{x}21', 25)
        if a % 24 == 0:
            print(x, a // 24)


def task14_MMigunov2026_4():  # 614
    s = -100
    xs = 0
    for x in range(1, 1078):
        n = 7 ** 77 + 7 ** 33 - x
        if str(n).count('0') > s:
            s = str(n).count('0')
            xs = x
    print(s, xs)


def task14_23967_5():
    for x in range(1, 5001):
        p = 7 * 13 ** 180 + 5 * 13 ** 120 - x
        n = sys(p, 13)
        if n.count('0') == 60:
            print(x)


def task14_LShastin2026_6():  # 20
    n = 5 * 729 ** 2024 + 3 * 243 * 1413 - 7 * 81 ** 169 - 2 * 9 ** 107 + 3017
    print(int(sys(n, 27)) // 26)
    print(sum(int(i) for i in '2100000000000000000000000000000000000000000000000000000000000000000012513320'))


def task14_24086_7():  # 233
    c = 0
    for x in range(1, 3001):
        n = sys(5 * 7 ** 156 + 3 * 7 ** 10 - x ** 31, 7)
        if n.count('0') == 15:
            print(x)
            c += 1
    print(c)


def task14_24232_8():  # 1513
    n = sys(2 * 16 ** 2020 + 9 * 16 ** 2021 - 2 * 4 ** 2022 + 8 ** 2023 - 2 * 2 ** 2024 - 65536, 16)
    print(n + '\n', n.count('15') + 2)


def task14_24073_9():  # 60
    n = 5 * 729 ** 2024 + 3 * 243 ** 1413 - 7 * 81 ** 169 - 2 * 9 ** 107 + 3017
    print(sys(n, 27))
    print(len(sys(n, 27)))


def task14_24048_10_f(s, p):
    s = s[::-1]
    return sum(int(s[i], 36) * p ** i for i in range(len(s)))


def task14_24048_10():  # 1529685
    for p in range(10, 10000):
        if (task14_24048_10_f('KOT', p) + task14_24048_10_f('GOLODNI', p)) \
                == (task14_24048_10_f('MEEOW', p) * task14_24048_10_f('100', p)) - 20194023088:
            print(task14_24048_10_f('purr', p))


def task14_23934_11():  # 159792
    for p in range(10, 37):
        n = int('2465123', p) + int('251341', p)
        if n % 17 == 0:
            print(n // 17)
            break


def task14_23753_12():  # 3319197720
    for x in printable[:29]:
        n = int(f'923{x}874', 29) + int(f'524{x}6152', 29)
        if n % 28 == 0:
            print(n // 28)


def task14_23391_13():  # 48
    n = 30 * 36 ** 231 + 18 * 6 ** 101 - 3 * 36 ** 45 - 2357
    c = 0
    while n > 0:
        ost = n % 36
        if int(ost % 5 == 0) + int(ost % 3 == 0) == 1:
            c += 1
        n //= 36
    print(c)


def task14_23373_14():  # 267
    n = 2 * 2401 ** 525 + 3 * 343 ** 524 - 4 * 49 ** 523 + 5 * 49 ** 522 - 6 * 7 ** 521 - 35
    c = 0
    while n > 0:
        ost = n % 49
        if ost <= 9:
            c += 1
        n //= 49
    print(c)


def task14_23390_15():  # 377
    n = 17 * 125 ** 453 + 117 * 5 ** 231 - 3 * 5 ** 13 - 2357
    c = 0
    while n > 0:
        ost = n % 125
        if ost <= 37:
            c += 1
        n //= 125
    print(c)


def task14_22067_16():  # 4
    A = []
    n = 3 * 17 ** 777 + 15 * 17 ** 250 - 6 * 17 ** 100 + 2
    while n > 0:
        ost = n % 17
        if ost % 2 == 0:
            A.append(ost)
        n //= 17
    print(len(set(A)))


def t14_23935_17_f(s, p):  # 819869
    s = s[::-1]
    return sum(int(s[i], 36) * p ** i for i in range(len(s)))


def task14_23935_17():
    for p in range(17, 100):
        if (t14_23935_17_f('22A12E', p) + t14_23935_17_f('2F1391', p) - t14_23935_17_f('1H05D0', p)) % 19 == 0:
            print((t14_23935_17_f('22A12E', p) + t14_23935_17_f('2F1391', p) - t14_23935_17_f('1H05D0', p)) // 19)
            break


def task14_19880_18():  # 25
    A = []
    n = 15625**16 - 3125**3 * 25**19 + 625**4 - 2005
    while n > 0:
        A.append(n % 25)
        n //= 25
    print(A.count(0))


def task14_lashin_19():  # 4
    n = 30 ** 30 + 443 * 900 ** 14 + 76 * 2700 ** 12 - 81000 ** 9
    c = 0
    while n > 0:
        ost = n % 30
        if ost > 15:
            c += 1
        n //= 30
    print(c)


def task14_bahtiev_20():  # 27
    for p in range(15, 37):
        n = int('DAD', p) + int('ABED', p) == int('BAD', p) + 206698
        if n:
            print(p)
task14_bahtiev_20()
