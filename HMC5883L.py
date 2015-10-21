"""
This program handles the communication over I2C
between a Raspberry Pi and a HMC5883L Digital Compass.
Made by: MrTijn/Tijndagamer
Released under the MIT License
Copyright 2015
"""

import smbus
from time import sleep

class HMC5883L:
    address = None
    bus = smbus.SMBus(1)

    # Registers
    CONF_REG_A = 0
    CONF_REG_B = 1
    MODE_REG = 2
    STATUS_REG = 9
    ID_REG_A = 10
    ID_REG_B = 11
    ID_REG_C = 12

    DATA_X_MSB = 3
    DATA_X_LSB = 4
    DATA_Z_MSB = 5
    DATA_Z_LSB = 6
    DATA_Y_MSB = 7
    DATA_Y_LSB = 8

    # Measurement modes
    MEA_MODE_NORM = 0
    MEA_MODE_POS = 1 # Postive bias for all axes
    MEA_MODE_NEG = 2 # Negative bias for all axes

    # Sample counts
    SAMPLE_COUNT_1 = 0 # default
    SAMPLE_COUNT_2 = 1
    SAMPLE_COUNT_4 = 2
    SAMPLE_COUNT_8 = 3

    def __init__(self, address = 0x1E):
        """Handles the I2C communication between a RPi and a HMC5883L.

        This is a WIP.
        """
        self.address = address

    def read_i2c_word(self, register):
        """Read two i2c registers and combine them.

        register -- the first register to read from.
        Returns the combined read results.
        """
        # Read the data from the registers
        high = self.bus.read_byte_data(self.address, register)
        low = self.bus.read_byte_data(self.address, register + 1)

        value = (high << 8) + low

        if (value >= 0x8000):
            return -((65535 - value) + 1)
        else:
            return value

    # Set methods

    def set_measurement_mode(self, new_mode):
        """Sets the sets measurement mode.

        new_mode -- the new measurement mode
        See datasheet page 12 table 6.
        """

        if new_mode != MEA_MODE_NORM or new_mode != MEA_MODE_POS or new_mode != MEA_MODE_NEG:
            print("Invalid new_mode")
            return

        return

    def set_typ_data_output_rate(self, new_rate):
        """Sets the typical data output rate.

        new_rate -- the new output.
        See datasheet page 12 table 5.
        """

        return

    def set_sample_count(self, new_count):
        """Sets the average sample count.

        new_count -- the new average sample count.
        See datasheet page 12 table 4.
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

    # Get methods

    def get_measurement_mode(self):
        """Reads and returns the current measurement mode.

        See datasheet page 12 table 6.
        """
        raw_data = self.bus.read_byte_data(self.address, self.CONF_REG_A)

        return raw_data

    def get_typ_data_output_rate(self):
        """Reads and returns the current typical data output rate.

        See datasheet page 12 table 5.
        """
        raw_data = self.bus.read_byte_data(self.address, self.CONF_REG_A)

        return raw_data

    def get_sample_count(self):
        """Reads and returns the current average sample count.

        See datasheet page 12 table 4.
        """
        raw_data = self.bus.read_byte_data(self.address, self.CONF_REG_A)

        return raw_data

    def get_operating_mode(self):
        """Reads and returns the current operating mode.

        See datasheet page 14 table 10, 11 and 12.
        """
        raw_data = self.bus.read_byte_data(self.address, self.MODE_REG)

        return raw_data

    def get_device_gain(self):
        """Reads and returns the current device gain.

        See datasheet page 13 table 9.
        """
        raw_data = self.bus.read_byte_data(self.address, self.CONF_REG_B)

        return raw_data

    def get_status(self):
        """Reads and returns the device status.

        See datasheet page 16 table 16 & 17.
        """
        raw_data = self.bus.read_byte_data(self.address, self.STATUS_REG)

        return raw_data

    def get_self_test_results(self):
        """Gets and returns the self test results."""

        self.bus.write_byte_data(self.address, self.CONF_REG_A, 0x70)
        self.bus.write_byte_data(self.address, self.CONF_REG_B, 0xA0)
        sleep(0.006)
        z_data = self.bus.read_word_data(self.address, self.DATA_Z_MSB)
        x_data = self.bus.read_word_data(self.address, self.DATA_X_MSB)
        y_data = self.bus.read_word_data(self.address, self.DATA_Y_MSB)

        return [x_data, y_data, z_data]

    def get_compass_data(self):
        """Reads and compensates and returns X, Y and Z values."""

        return