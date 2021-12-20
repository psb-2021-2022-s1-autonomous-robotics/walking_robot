from microbit import *



def turn(pin, angle, cw, period = 10):
    """turn servo on pin to angle."""
    if cw:
        start=0.55
        end=2.3
    else:
        start=2.3
        end=0.55
    eq = (((end-start)/180)*angle)+start
    pin.write_analog(eq/period * 1023)


pin16.set_analog_period(10)
pin15.set_analog_period(10)
    
while True:
    turn(pin15, 180, True)
    turn(pin16, 180, False)
    sleep(1000)
    turn(pin15, 90, False)
    turn(pin16, 90, True)
    sleep(1000)
    turn(pin15, 90, True)
    turn(pin16, 180, False)
