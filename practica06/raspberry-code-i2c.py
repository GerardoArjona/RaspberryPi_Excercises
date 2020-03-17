#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ## #############################################################
#
# Author: Mauricio Matamoros
# Date:
#
# ## ############################################################
# Future imports (Python 2.7 compatibility)
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import smbus2
from datetime import datetime
from struct import *
import time
from itertools import count
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from multiprocessing import Process

# Arduino's I2C device address
SLAVE_ADDR = 0x05 # I2C Address of Arduino 1

# Name of the file in which the log is kept
LOG_FILE = './temp.log'

# Initialize the I2C bus;
# RPI version 1 requires smbus.SMBus(0)
i2c = smbus2.SMBus(1)

plt.style.use('fivethirtyeight')

x_values = []
y_values = []

index = count()


def animate(i):
	with open(LOG_FILE, 'r') as fp:
		last = fp.readlines()[-1]
	temp = last.split(" ")[1]
	temp = float(temp.replace("°C","").strip())
	time = last.split(" ")[0]
	time = datetime.fromtimestamp(float(time))
	x_values.append(str(time.strftime('%H:%M:%S')))
	y_values.append(temp)
	plt.cla()
	plt.plot(x_values, y_values)
	plt.rcParams["font.size"] =11
	plt.rcParams['xtick.major.pad'] = 8
	plt.ylabel('Temperture °C')
	plt.xlabel('Time')
	plt.xticks(rotation=45)
	plt.ylim(-5, 100)	

def readTemperature():
	try:
		msg = smbus2.i2c_msg.read(SLAVE_ADDR, 4)
		i2c.i2c_rdwr(msg)
		data = list(msg)

		#python 2: 
		#temp = unpack('<f', ''.join([chr(c) for c in data]))

		#python 3:
		temp = unpack('<f', bytes(data))
		#print('Received temp: {} = {}'.format(data, temp))
		return temp
	except Exception as e:
		#print("Exception")
		#print(e)
		return None

def log_temp(temperature):
	try:
		temperature = str(temperature).replace("(","").replace(")","").replace(",","")
		t = float(temperature)
		#print(t)
		print('{} °C\n'.format(temperature))
		with open(LOG_FILE, 'a+') as fp:
			fp.write('{} {}°C\n'.format(
				time.time(),
				temperature
			))
		return temperature
	except  Exception as e:
		print(e)
		return

def main():
	while True:
		try:
			cTemp = readTemperature()
			t = log_temp(cTemp)
			time.sleep(1)
		except KeyboardInterrupt:
			return
		
def graph():
	plt.axis([0, 10, -10, 100])
	#plt.setp(ax.get_xticklabels(), rotation=30, horizontalalignment='right')
	ani = FuncAnimation(plt.gcf(), animate, 1000)
	plt.tight_layout()
	plt.show()

if __name__ == '__main__':

	p1 = Process(target=main, args=())
	p1.start()
	p2 = Process(target=graph, args=())
	p2.start()