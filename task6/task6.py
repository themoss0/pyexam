from turtle import *

def task6_1():
    f = 5
    for _ in range(5):
        forward(40*f); right(90); fd(46*f); rt(90)
    up()
    fd(19*f); rt(90); fd(19); rt(90)
    down()
    for _ in range(5):
            fd(37); rt(90); fd(19); rt(90)

    up()
    for x in range(0, 5000, 50):
        for y in range(0, 5000, 50):
            goto(x, y)
            dot(3, 'red')
            up()

def task6_19238_2(): # 187
    l = 10
    left(90)
    speed(50000)

    for _ in range(8):
          fd(16*l); rt(90); fd(22*l); rt(90)
    up()

    fd(5*l); rt(90); fd(5*l); lt(90)

    down()

    for _ in range(8):
         fd(52*l); rt(90); fd(77*l); rt(90)
    up()
    for x in range(0, 40):
         for y in range(0, 17):
              goto(x*l, y * l)
              dot(3, 'red')

def task6_MMigunov2026_3(): #36
    l = 15
    lt(90)
    speed(50000)

    for _ in range(2):
         fd(3*l); rt(90); fd(20*l); rt(90)
    up()
    backward(8*l); rt(90); fd(9*l);lt(90)
    down()
    for _ in range(2):
         fd(16*l); rt(90); fd(8*l); rt(90)
    up()    
    for x in range(0, 30):
        for y in range(-10, 10):
             goto(x*l, y*l)
             dot(3, 'red')
    tracer()
    done()

def task6_23959_4(): #330
    l = 15
    lt(90)
    speed(5000)
    for _ in range(2):
        fd(20*l); lt(270); backward(15*l); rt(90)
    up()
    fd(10*l); rt(90); backward(20*l); lt(90)
    down()
    for _ in range(2):
        fd(6*l); rt(90); fd(6*l); rt(90)
    up()
    for x in range(-20, 10):
         for y in range(0, 30):
              goto(x*l, y*l)
              dot(3, 'red')
    tracer()
    done()

def task6_DBahtiev_5():
    l = 8
    lt(90)
    speed(5000)

    for _ in range(5):
        fd(42*l); rt(270); fd(55*l); lt(90)
    up()
    fd(17*l); rt(90); fd(12*l); lt(90)
    down()
    for _ in range(14):
        fd(14*l); lt(90); fd(200*l); lt(90)
    up()
    for x in range(-60, 10):
        for y in range(0, 30):
            goto(x*l, y*l)
            dot(3, 'red')
    tracer()
    done()


def task6_24060_6(): # 48
    lt(90)
    l = 8
    speed(5000)

    for _ in range(3):
        fd(25 * l); lt(90); fd(30*l); lt(90)
    up()
    fd(20*l); rt(90); backward(7 * l); lt(90)
    down()

    for _ in range(3):
        fd(60*l); rt(90); fd(30*l); rt(90)
    up()
    for x in range(-30, 20):
        for y in range(-20, 20):
            goto(x*l, y*l)
            dot(3, 'red')
    tracer()
    done()

def task6_24224_7():
    lt(90)
    l = 14
    speed(5000)

    for _ in range(3):
        for _ in range(2):
            fd(13*l); rt(90); fd(10*l); rt(90)
        up()
        fd(5*l); rt(90); back(4*l); lt(90)
        down()
    up()
    for x in range(-10, 20):
        for y in range(0, 20):
            goto(x*l,y*l)
            dot(3, 'red')
    tracer()
    done()


def task6_24101_8(): # 840
    lt(90)
    l = 15
    speed(100000)

    for _ in range(5):
        fd(42*l); rt(270); fd(55*l); lt(90)
    up()
    fd(17*l); rt(90); fd(12*l); lt(90)
    down()
    for _ in range(14):
        fd(14*l); lt(90); fd(200*l); lt(90)
    up()
    for x in range(-60, 60):
        for y in range(0, 27):
            goto(x*l, y*l)
            dot(3, 'red')
    tracer()
    done()


def task6_lashin_9():  # 11
    lt(90)
    l = 20
    speed(5000)

    rt(173)
    for _ in range(200):
        fd(1*l); lt(30)

    up()
    for x in range(0, 20):
        for y in range(-5, 5):
            goto(x*l, y*l)
            dot(3, 'red')
    tracer()
    done()


def task6_shastin_10():
    lt(90)
    l = 16
    speed(5000)

    down()

    fd(5*l)
    rt(60)
    for _ in range(6):
        fd(23*l); rt(45); fd(17*l); rt(135)
    lt(90); fd(7*l)

    up()

    for x in range(0, 40):
        for y in range(0, 20):
            goto(x*l, y*l)
            dot(3, 'red')
    tracer()
    done()


def task6_23803_11():  # 3+3+3+3 = 12
    lt(90)
    l = 25
    speed(5000)
    down()

    for _ in range(2):
        fd(6 * l); lt(270); back(20 * l); rt(90)
    up()
    fd(3 * l); rt(90); back(3 * l); lt(90)
    down()
    for _ in range(2):
        fd(15 * l); rt(90); fd(70 * l); rt(90)

    up()

    for x in range(-20, 20):
        for y in range(-20, 20):
            goto(x*l, y*l)
            dot(3, 'red')
    tracer()
    done()


def task6_24854_11():
    l = 11
    lt(90)
    speed(5000)

    for _ in range(4):
        fd(20*l); rt(90); fd(120*l); rt(90)
    up()
    fd(12*l); rt(90); fd(3*l); lt(90)
    down()
    for _ in range(3):
        fd(25*l); rt(90); fd(23*l); rt(90)

    up()

    for x in range(0, 30):
        for y in range(0, 30):
            goto(x*l, y*l)
            dot(3, 'red')
    tracer()
    done()

task6_24854_11()