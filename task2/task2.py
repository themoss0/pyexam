# this is my practise file of task number 2


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


def task2_iglin_12():  # wzyx
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
task2_bahtiev_13()