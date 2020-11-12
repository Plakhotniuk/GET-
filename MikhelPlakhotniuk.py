#I can change file!!!
import RPi.GPIO as GPIO
import time
import math

GPIO.setmode(GPIO.BCM)
leds = [24, 25, 8, 7, 12, 16, 20, 21]
leds2 = [21, 20, 16, 12, 7, 8, 25, 24]

for m in leds:
    GPIO.setup(m,GPIO.OUT)

def lightUp(ledNumber, period):
    GPIO.output(leds[ledNumber], 1)
    time.sleep(period)
    GPIO.output(leds[ledNumber], 0)

def blink (ledNumber, count, period):
    n = 0
    while n < count:
        lightUp(ledNumber, period)
        time.sleep(period)
        n += 1

def runingLight(count, period):
    for n in range(count):
        for m in range(8):
            lightUp (m , period)

def runningDark (count, period):
    for u in leds:
        GPIO.output(u, 1)
    for n in range(count):
        for m in range(8):
            GPIO.output(leds[m], 0)
            time.sleep(period)
            GPIO.output(leds[m], 1)

def decToBinList (decNumber):
    return [int(i) for i in bin(decNumber)[2:].zfill(8)]

def lightNumber (decNumber):
    a = decToBinList(decNumber)
    for i in range(8):
        GPIO.output(leds2[i], a[i])
    time.sleep(10)

print(decToBinList (130))
lightNumber(130)

GPIO.cleanup()
