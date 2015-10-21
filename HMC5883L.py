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

    def set_measurement_mode(self, new_mode):
        """Sets the sets measurement mode.

        new_mode -- the new measurement mode
        See datasheet page 12 table 6.
        """

        return

    def set_typ_data_output_rate(self, new_rate):
    	"""Sets the typical data output rate.

    	new_rate -- the new output. See datasheet page 12 table 5.
    	"""

        return

    def set_operating_mode(self, new_mode):
    	"""Sets the operating mode.

        new_mode -- the new operating mode. new_mode can be:
        0: The device will be set to continuous measurement mode.
        1: The device will be set to single measurement mode (default).
        2: The device will be set to idle.
        See datasheet page 14 table 10, 11 and 12.
        """

        return

    def set_device_gain(self, new_gain):
    	"""Sets the device gain.

        new_gain -- the new gain.
        See datasheet page 13 table 9.
        """

        return

    def get_status(self):
    	"""Reads and returns the device status.

        See datasheet page 16 table 16 & 17.
    	"""

    	return

    def get_compass_data(self):
    	"""Reads and compensates and returns X, Y and Z values."""

        return