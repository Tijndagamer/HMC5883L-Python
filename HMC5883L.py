"""
This program handles the communication over I2C
between a Raspberry Pi and a HMC5883L Digital Compass.
Made by: MrTijn/Tijndagamer
Released under the MIT License
Copyright 2015
"""

import smbus

class HMC5883:
    address = None
	bus = smbus.SMBus(1)

	# Registers
	CONF_REG_A = 0
	CONF_REG_B = 1
	MODE_REG = 2
	ID_REG_A = 10
	ID_REG_B = 11
	ID_REG_C = 12

	DATA_X_MSB = 3
	DATA_X_LSB = 4
	DATA_Z_MSB = 5
	DATA_Z_LSB = 6
	DATA_Y_MSB = 7
	DATA_Y_LSB = 8
	STATUS_REG = 9

	def __init__(self, address):
		"""Handles the I2C communication between a RPi and a HMC5883L.

        This is a WIP.
		"""
        self.address = address

