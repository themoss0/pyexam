# this is my practise file of task number 5

def sys(num, ss):
    res = ''
    while num > 0:
        res = str(num % ss) + res
        num //= ss
    return res


def task5_23437_1():
    for n in range(1, 1001):
        n_3 = sys(n, 3)
        if n % 3 == 0:
            n_3 = '1' + n_3 + '02'
        if n % 3 != 0:
            n_3 = n_3 + sys(((n % 3) * 4), 3)
        r = int(n_3, 3)
        if r < 199:
            print(n)


def task5_21404_2():
    for n in range(1, 501):
        b = bin(n)[2:]
        if b.count('1') % 2 == 0:
            b = b + '0'
            b = '10' + b[2:]
        else:
            b = b + '1'
            b = '11' + b[2:]
        r = int(b, 2)
        if r > 480:
            print(n, r)
            break


def task5_20896_3():  # 8
    for n in range(1, 1001):
        b = bin(n)[2:]
        if b.count('0') % 2 == 0:
            b = b + '0'
            b = '10' + b[2:]
        else:
            b = b + '1'
            b = '11' + b[2:]
        r = int(b, 2)
        if r > 19:
            print(n, r)


def task5_23551_4():  # 6
    for n in range(1, 1001):
        b = bin(n)[2:]
        if n % 2 == 0:
            b = '10' + b
        else:
            b = '1' + b + '01'
        r = int(b, 2)
        if r < 30:
            print(n, r)


def task5_19237_5():  # 222
    for n in range(1, 1001):
        t = sys(n, 3)
        if n % 3 == 0:
            t = t + t[-2:]
        else:
            t = t + sys((sum([int(x) for x in t])), 3)
        r = int(t, 3)
        if r % 2 == 0 and r > 220:
            print(r)


def task5_MMigunov2026_6():  # 41610
    res = []
    for n in range(1, 1235):
        p = sys(n, 5)
        if n % 5 == 0:
            p = sys(sum([int(x) for x in str(n % 52)]), 5) + p
        else:
            p = p[0] + p
        r = int(p, 5)
        res.append(r)
    print(max(res))


def task5_23958_7():  # 7
    for n in range(1, 1000):
        b = bin(n)[2:]
        if n % 4 == 0:
            b = b + b[:2]
        else:
            b = b + bin((n % 4) + 1)[2:]
        r = int(b, 2)
        if r >= 50:
            print(n, r)


def task5_DBahtiev_8():  # 30
    for n in range(1, 1001):
        t = sys(n, 3)
        if n % 5 == 0:
            t = t + t[-2:]
        else:
            t = t + sys(((n % 5) * 7), 3)
        r = int(t, 3)
        if r <= 273:
            print(r, n)


def task2_24059_9():  # 5
    for n in range(1, 1000):
        t = sys(n, 3)
        if n % 3 == 0:
            t = t + '10'
        else:
            t = t + sys(((n % 3) * 5), 3)
        r = int(t, 3)
        if r > 130:
            print(r, n)
            break
def task5_24223_10(): # 25
    for n in range(1, 1001):
        b = bin(n)[2:]
        if n % 2 != 0:
            b = b[-1] + b[1:-1] + b[0] + '0'
        else:
            b = b + '0'
        r = int(b, 2)
        if r >= 50:
            print(r, n)
            break

def task5_24100_11(): # 30
    for n in range(1, 1001):
        t = sys(n, 3)
        if n % 5 == 0:
            t = t + t[-2:]
        else:
            t = t + sys(((n%5) * 7), 3)
        r = int(t, 3)
        if r <= 273:
            print(f'{n=}, {r=}')


def task5_iglin_12():  # 40
    for n in range(7, 1000):
        b = bin(n)[2:]
        if b.count('1') % 3 == 0:
            b = b + b[-2:]
        else:
            b = b + bin((int(b) % 3) * 3)[2:]
        r = int(b, 2)
        if r >= 300:
            print(n)
            break

