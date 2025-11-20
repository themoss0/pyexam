# this is my practise file of task number 2
from itertools import product, permutations

def task2_23431_1():
    print('w x y z')
    for w in range(2):
        for x in range(2):
            for y in range(2):
                for z in range(2):
                    F = not (y <= x) or (z <= w) or not (z)
                    if not F:
                        print(w, x, y, z)


def task2_21401_2():
    print('w x y z')
    for w in range(2):
        for x in range(2):
            for y in range(2):
                for z in range(2):
                    f = x and (z <= w) and (not (y))
                    if f:
                        print(w, x, y, z)


def task2_20894_3():  # xyzw
    print('w x y z')
    for w in range(2):
        for x in range(2):
            for y in range(2):
                for z in range(2):
                    f = (not (x <= y)) or (z <= w) or (not (z))
                    if not f:
                        print(w, x, y, z)


def task2_23548_4():  # wyxz
    print('w x y z')
    for w in range(2):
        for x in range(2):
            for y in range(2):
                for z in range(2):
                    f = ((x or y) <= z) or (y == w) or z
                    if not f:
                        print(w, x, y, z)


def task2_19234_5():
    print('w x y z')
    for w in range(2):
        for x in range(2):
            for y in range(2):
                for z in range(2):
                    f = not ((not (x) or y) and (not (w))) or not (z and not (y and w))
                    if not f:
                        print(w, x, y, z)


def task2_MMigunov2026_6():  # wzyx
    print('w x y z')
    for w in range(2):
        for x in range(2):
            for y in range(2):
                for z in range(2):
                    f = not (x <= z) or (w <= (y == z))
                    if not f:
                        print(w, x, y, z)


def task2_23955_7():  # wyzx
    print('w x y z')
    for w in range(2):
        for x in range(2):
            for y in range(2):
                for z in range(2):
                    f = (x and y and (not (z))) or ((not (w)) and y and z)
                    if f:
                        print(w, x, y, z)


def task2_DBahtiev_8():  # yzwx
    print('w x y z')
    for w in range(2):
        for x in range(2):
            for y in range(2):
                for z in range(2):
                    f = z or (x == (y <= w))
                    if not f:
                        print(w, x, y, z)


def task2_24090_9():
    print('w x y z')
    for w in range(2):
        for x in range(2):
            for y in range(2):
                for z in range(2):
                    f = ((not w) <= x) <= (y and z) and (x == (not(w)))
                    if f:
                        print(w, x, y, z)

def task2_24220_10(): # yxzw
    print('w x y z')
    for w in range(2):
        for x in range(2):
            for y in range(2):
                for z in range(2):
                    f = w and (not(y)) and ((not(x)) or z)
                    if f:
                        print(w, x, y, z)

def task2_24099_11(): #yzwx
    print('w x y z')
    for w in range(2):
        for x in range(2):
            for y in range(2):
                for z in range(2):
                    F = z or (x == (y <= w))
                    if not F:
                        print(w, x, y, z)


def task2_iglin_12():  # yzwx
    print('w x y z')
    for w in range(2):
        for x in range(2):
            for y in range(2):
                for z in range(2):
                    f = not(y <= (x == w)) and (z <= x)
                    if f:
                        print(w, x, y, z)


def task2_bahtiev_13():  # xwzy
    print('w x y z')
    for w in range(2):
        for x in range(2):
            for y in range(2):
                for z in range(2):
                    f = (y <= x) and (not(z <= (x == w)))
                    if f:
                        print(w, x, y, z)


def task2_24419_14(): # zwxy
    # new method:
    # (y → z) ∧ ¬((y ∨ w) → (z ∧ x))
    for x1, x2, x3, x4, x5 in product([0, 1], repeat=5):
        t = (
            (1, 1, x1, 1, 1),
            (x2, 1, 1, x3, 1),
            (1, 1, x4, x5, 1)
        )
        if len(t) == len(set(t)):
            for p in permutations('xyzw', r=4):
                if all(task2_24419_14_f(**dict(zip(p, line))) == line[-1] for line in t):
                    print(*p)


def task2_24419_14_f(x, y, z, w):
    return (y <= z) and (not (y or w) <= (z and x))

def task2_23186_15():
    # new method:
    # (x→y)∧z∧¬w
    for x1, x2, x3, x4, x5, x6 in product([0, 1], repeat=6):
        t = (
            (0, 1, x1, x2, 1),
            (1, 1, x3, x4, 1),
            (1, x5, 1, x6, 1)
        )
        if len(t) == len(set(t)):
            for p in permutations('xywz', r=4):
                if all(task2_23186_15_f(**dict(zip(p, line))) == line[-1] for line in t):
                    print(*p)

def task2_23186_15_f(x, y, w, z):
    return (x <= y) and z and (not w)


def task2_21401_16():
    for x1, x2, x3, x4, x5, x6, x7 in product([0,1], repeat=7):
        t = (
            (x1, x2, 1, x3, 1),
            (x4, 1, 0, x5, 1),
            (1, 0, x6, x7, 1)
        )
        if len(t) == len(set(t)):
            for p in permutations('xyzw', r=4):
                if all(task2_21401_16_f(**dict(zip(p, line))) == line[-1] for line in t):
                    print(*p)

def task2_21401_16_f(x, y, z, w):
    #F = z∨(z≡w)∨¬(y→x)
    return x and (z <= w) and (not(y))


def task2_bahtiev_17_f(x, y, z, w):
    return (y <= x) and (not(z <= (x == w)))


def task2_bahtiev_17(): # x w z y
    for x1, x2, x3, x4, x5, x6, x7 in product([0,1], repeat=7):
        t = (
            (0, x1, x2, 0, 1),
            (1, x3, x4, x5, 1),
            (x6, 0, x7, 0, 1)
        )
        if len(t) == len(set(t)):
            for p in permutations('xyzw', r=4):
                if all(task2_bahtiev_17_f(**dict(zip(p, line))) == line[-1] for line in t):
                    print(*p)


def task2_lashin_18_f(m, e, o, w):
    return (m <= e) or (o == e) and w


def task2_23725_18():  # o e m w
    for x1, x2, x3, x4 in product([0, 1], repeat=4):
        t = (
            (1, 0, 1, 1, 0),
            (1, x1, x2, x3, 0),
            (0, x4, 1, 0, 0)
        )
        if len(t) == len(set(t)):
            for p in permutations('meow', r=4):
                if all(task2_lashin_18_f(**dict(zip(p, line))) == line[-1] for line in t):
                    print(*p)
