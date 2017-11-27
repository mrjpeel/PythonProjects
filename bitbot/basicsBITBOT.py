from microbit import *
import neopixel
from random import randint

leftspd = pin0
leftdir = pin8
rightspd = pin1
rightdir = pin12

count = 0
np = neopixel.NeoPixel(pin13, 12)


while True:
    red = randint(1,40)
    green = randint(1,40)
    blue = randint(1,40)
    leftspd.write_digital(1)
    leftdir.write_digital(0)
    if count < 13:
        for led in range(0,12):
            np[led] = (red, green, blue)
            np.show()
            sleep (100)
            count = count + 1
    else:
        count = 0