#!/usr/bin/env python3
# Future imports (Python 2.7 compatibility)
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(32, GPIO.OUT, initial=GPIO.LOW)
pwm = GPIO.PWM(32, 1000)

pwm.start(0)
flag = True
while flag:
    try:
        for i in range(0,101):
            sleep(0.05)
            pwm.ChangeDutyCycle(i)
            print(i)
            if(i == 100):
                print("full pwm")
                sleep(1)
        for j in range(100,-1,-3):
            print("down")
            print(j)
            sleep(0.1)
            pwm.ChangeDutyCycle(j)
            if(j == 1):
                flag = False
    except:
        print("flag false")
        flag = False
        pwm.ChangeDutyCycle(0)
	#end try
#end while
pwm.stop()
GPIO.cleanup()

