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

# El siguiente código hace parpadear el led
def ledsVarSpeed():
    print("Marquee right to left...")
    pins = [32, 26, 24, 22, 18, 16, 12]

    # Desactivar advertencias (warnings)
    # GPIO.setwarnings(False)
    # Configurar la librería para usar el número de pin.
    # Llame GPIO.setmode(GPIO.BCM) para usar el canal SOC definido por Broadcom
    GPIO.setmode(GPIO.BOARD)

    # Configurar el pin 32 como salida y habilitar en bajo
    GPIO.setup(pins, GPIO.OUT, initial=GPIO.LOW)

    # print("De 0.1 a 0.8")
    # print("Ingrese la velocidad que desea:")
    # speed = input()
    for pin in pins[::-1]:   
        GPIO.output(pin, GPIO.HIGH) # Enciende el led        
        sleep(0.1)            # Espera 500ms
        GPIO.output(pin, GPIO.LOW)  # Apaga el led

    return 0