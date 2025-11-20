def task7_23435_1():
    scr_size = 2560*1440
    i = 32
    scr_size_compressed = 1920*1080
    i_compressed = 31
    count = 110
    res1 = scr_size * i 
    res2 = scr_size_compressed * i_compressed
    res = res1 * 110 - res2 * 110
    print(res / 8 / 1024)

def task7_21406_2():
    size = 3840 * 2160
    i = 17
    size_c = 1280*720
    i_c = 5
    count = 120
    res1 = size * i
    res2 = size_c * i_c
    print(((res1 - res2) * 120) / 8 / 1024)

def task7_17861_3(): #41
    size = 1024 * 768
    i = 12
    speedbps = 1_310_720
    t = 300
    r1 = speedbps * t
    r2 = size * i
    print(r1 / r2)

def task7_23553_4(): # 396000
    size = 1920 * 1080
    i = 32
    size_c = 1280*1024
    i_c = 30
    count = 120
    res1 = size * i
    res2 = size_c * i_c
    print(((res1-res2) * 120) / 8 / 1024)

def task7_19239_5(): # 292
    size = 3840*2160
    i = 24
    c = 3742
    max_memb = 16 * 1024 * 1024 * 1024 * 8
    memb = c * i * size
    print(memb / max_memb)
    print(memb, max_memb*5)
    print('-----')
    print(c % ((max_memb) // (size * i)))

def task7_MMigunov_6(): #1395
    size = 3840*2160
    i = 23
    size_c = 2560*1440
    i_c = 20
    c = 100
    res1 = size * i 
    res2 = size_c * i_c
    print(int(((res1 - res2) * c) / 8 / 1024 / 1024))

def task7_23960_7(): #242850
    size = 1600 * 1200
    i = 24
    size_c = 1024 * 768
    i_c = 8
    c = 50
    res1 = size*i
    res2 = size_c * i_c
    print(((res1-res2) * c)/ 8/ 1024)

def task7_DBahtiev_8(): #12.8 -> 12
    ch = 4
    d = 32_000
    i = 64
    ch_c = 2
    d_c = 16000
    i_c = 20
    memo = (ch*d*i)
    memc = (ch_c *d_c * i_c)
    print(memo, memc)
    print(memo // memc)

def task7_241007_9(): # 73728
    pass # решил на бумаге
    # принцип решения основан на представлении данных величин как несколько предыдущих (к примеру, d2 = 2 * d1, i2 = 3* 0.5 * i1)


def task7_24225_10(): # 48
    size = 1920 * 1080
    i = 24
    c = 100
    mem = size * i * c
    speedb = 67_108_864

    print((mem * 0.65) / speedb)


def task7_24102_11(): # 12.8 -> 12
    ch = 4
    discr = 32_000
    i = 64
    ch_i = 2
    discr_i = 16_000
    i_i = 20
    mem1 = ch * discr * i * 1
    mem2 = ch_i * discr_i * i_i * 1
    print(mem1 / mem2)


def task7_iglin_12():
    ch = 2
    memmb = 70
    ch_i = 4
    d = 5
    comp = 0.75


def task7_bahtiev_13():  # 2660
    size = 3072*4096
    i = 24
    c = 150
    membit = size * i * c
    speedbit = 4 * 1024 * 1024 * 8
    mem_comp = membit * 0.5
    t_comp = 0.1 * 150

    print(f'1: {membit / speedbit}')
    print(f'2: {mem_comp / speedbit + t_comp}')
    print((membit / speedbit) - (mem_comp / speedbit + t_comp))


def task7_23804_14():  # 27.962026......... => 28
    t_sec = 3 * 3600
    ch = 2
    d = 60_000
    i = 10
    speedMb = 4
    speedBit = speedMb * 1024 * 1024 * 8
    print((t_sec * d * ch * i), (speedBit * t_sec) / (t_sec * d * ch * i))
