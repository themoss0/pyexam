from sys import setrecursionlimit, set_int_max_str_digits

# this is my practise file of task number 16
setrecursionlimit(1000000)
set_int_max_str_digits(100000)


def task16_23426_1_G(n):
    if n <= 20:
        return n
    if n > 20:
        return task16_23426_1_G(n - 2) + 1


def task16_23426_1_F(n):
    return task16_23426_1_G(n - 3)


def task16_21415_2_F(n):
    if n <= 5:
        return 1
    if n > 5:
        return n + task16_21415_2_F(n - 2)


def task16_23562_3_G(n):
    if n <= 9:
        return 3 * n
    if n > 9:
        return task16_23562_3_G(n - 2) + 1


def task16_23562_3_F(n):  # 24017
    return task16_23562_3_G(n - 1)


def task16_19248_4_F(n):  # 757543052
    if n < 5:
        return n
    if n >= 5:
        return 2 * n * task16_19248_4_F(n - 4)


def task16_MMigunov2026_5_F(n):
    if n >= 9876:
        return task16_MMigunov2026_5_F(n + 777)
    if n < 9876:
        return n * 2 + task16_MMigunov2026_5_F(n + 2)


def task16_23969_6_G(n):
    if n < 8:
        return 3 * n
    if n >= 8:
        return task16_23969_6_G(n - 3) + 2


def task16_23969_6_F(n):  # 24732
    return 3 * (task16_23969_6_G(n - 4) + 5)


def task16_DBahtiev2026_7_G(n):  # 66503
    if n >= 30000:
        return 3
    if n < 30000:
        return task16_DBahtiev2026_7_G(n + 3) + 7


def task16_DBahtiev2026_7_F(n):
    return task16_DBahtiev2026_7_G(n + 1)


def task16_24064_8_F(n):  # 39180999964189790209830417 ?????
    if n <= 3:
        return n + 3
    if n > 3:
        return (task16_24064_8_F(n - 1) + 2 * task16_24064_8_F(n - 2)) - task16_24064_8_F(n - 3)


def task16_24234_9(n):  # 1605511072
    if n < 15:
        return n
    if n >= 15:
        return (n - 8) * task16_24234_9(n - 6)


def task16_24114_10_G(n):  # 66503
    if n >= 30000:
        return 3
    return task16_24114_10_G(n + 3) + 7


def task16_24114_10_F(n):
    return task16_24114_10_G(n + 1)


def task16_18123_11(n):
    if n >= 2010:
        return n
    if n < 2010:
        return (task16_18123_11(n+3) + task16_18123_11(n+2) + task16_18123_11(n + 1))


def task16_lashin_12(n):  # 66048
    if n < 10:
        return n + 10
    return task16_lashin_12(n-8) + 2 ** n


def task16_bahtiev_13_G(n):  # 17937
    return task16_bahtiev_13_F(n-3)


def task16_bahtiev_13_F(n):
    if n <= 20:
        return 177
    return task16_bahtiev_13_G(n-2) + 4


def task16_24081_14_F(n):
    return task16_24081_14_G(n - 50000) + task16_24081_14_G(n + 50000)

def task16_24081_14_G(n):  #152076
    if n <= 6:
        return 5 ** n
    return task16_24081_14_G(n-3) + 2
print(task16_24081_14_F(100000))