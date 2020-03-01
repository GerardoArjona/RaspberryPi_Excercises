#!/usr/bin/env python3
# ## ###############################################
#
# pwm.py
# Blinks a led on pin 32 using Raspberry Pi
#
# Autor: Mauricio Matamoros
# License: MIT
#
# ## ###############################################

# Future imports (Python 2.7 compatibility)
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

# Importa la librería de control del GPIO de la Raspberry Pi
import RPi.GPIO as GPIO
# Importa la función sleep del módulo time
from time import sleep

def num_led(num):
	print("Leds")
	print(num)
	pins = [32, 26, 24, 22, 18, 16, 12]

    # Desactivar advertencias (warnings)
    # GPIO.setwarnings(False)
    # Configurar la librería para usar el número de pin.
    # Llame GPIO.setmode(GPIO.BCM) para usar el canal SOC definido por Broadcom
	GPIO.setmode(GPIO.BOARD)

    # Configurar el pin 32 como salida y habilitar en bajo
	GPIO.setup(pins, GPIO.OUT, initial=GPIO.LOW)

    # El siguiente código hace parpadear el led
	if num == 1:
		GPIO.output(32, GPIO.HIGH) # Enciende el led
	elif num == 2:
		GPIO.output(26, GPIO.HIGH) # Enciende el led
	elif num == 3:
		GPIO.output(24, GPIO.HIGH) # Enciende el led
	elif num == 4:
		GPIO.output(22, GPIO.HIGH) # Enciende el led
	elif num == 5:
		GPIO.output(18, GPIO.HIGH) # Enciende el led
	elif num == 6:
		GPIO.output(16, GPIO.HIGH) # Enciende el led
	elif num == 7:
		GPIO.output(12, GPIO.HIGH) # Enciende el led

	return 0