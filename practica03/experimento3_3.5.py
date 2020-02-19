#!/usr/bin/env python3
# ## ###############################################
#
# pwm.py
# Controls a 7-segments display using Raspberry Pi
# and a 74LS47 driver
#
# Autor: Mauricio Matamoros
# License: MIT
#
# ## ###############################################

# Future imports (Python 2.7 compatibility)
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import sys

# Importa la librería de control del GPIO de la Raspberry Pi
import RPi.GPIO as GPIO
# Importa la función sleep del módulo time
from time import sleep

# Desactivar advertencias (warnings)
# GPIO.setwarnings(False)
# Configurar la librería para usar el número de pin.
GPIO.setmode(GPIO.BOARD)
# Configurar pines 36, 38, 40 y 37 como salida y habilitar en bajo
GPIO.setup(36, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(38, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(40, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(37, GPIO.OUT, initial=GPIO.LOW)

# Mapea bits a los pines de la GPIO
def bcd7(num):
	GPIO.output(36, GPIO.HIGH if num & 0x00000008 else GPIO.LOW )
	GPIO.output(38, GPIO.HIGH if num & 0x00000004 else GPIO.LOW )
	GPIO.output(40, GPIO.HIGH if num & 0x00000002 else GPIO.LOW )
	GPIO.output(37, GPIO.HIGH if num & 0x00000001 else GPIO.LOW )

def pingPongBCD():
	flag = True
	nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
	print("De 0.1 a 0.9")
	print("Ingrese la velocidad que desea:")
	speed = input()
	while flag:
		try:
			for i in range(0, len(nums)):
				sleep(float(speed)) 
				bcd7(nums[i])
		except:
			flag = False
			print(sys.exc_info())
			#end try
		#end while

	# Reinicia los puertos GPIO (cambian de salida a entrada)
	GPIO.cleanup()

pingPongBCD()