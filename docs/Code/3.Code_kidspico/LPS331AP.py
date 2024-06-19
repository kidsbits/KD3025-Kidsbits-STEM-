'''
LPS331AP 1.0
'''

from machine import Pin
from machine import I2C
#import numpy as np
import time
import math
# import ustruct


LPS331AP_I2C_ADDR = 0x5D            
WHO_AM_I_REG = 0x0F

REF_P_XL = 0x08        #Pressure reference value
REF_P_LR = 0x09
REF_P_HR = 0x0A
RES_CONF = 0x10        #Pressure resolution
CTRL_REG1 = 0x20        #Data control register
CTRL_REG2 = 0x21        #Memory control register

CTRL_REG3 = 0x22        #Interrupt control register
INTERRUPT_CFG = 0x23        #Interrupt configuration
INT_SOURCE = 0x24        #Interrupt source
THS_P_L = 0x25        #Interrupt Pressure Threshold (LSB)
THS_P_HT = 0x26
STATUS_REG = 0x27        #Status register

PRESS_OUT_XLP = 0x28        #pressure data [7:0]
PRESS_OUT_LP = 0x29        #pressure data [15:8]
PRESS_OUT_H = 0x2A        #pressure data [23:16]

TEMP_OUT_L = 0x2B        #temperature data
TEMP_OUT_H = 0x2C
AMP_CTELA = 0x2D        #Analog operational amplifier data acquisition current control

DELTA_PRESS_XL = 0x3C        #Pressure deviation[7:0]
DELTA_PRESS_L1 = 0x3D        #Pressure deviation[15:8]
DELTA_PRESS_L2 = 0x3E        #Pressure deviation[23:16]
CHIP_ID = 0xBB


class lps331ap:
    def __init__(self, bus, scl, sda):
        self.bus = bus
        self.scl = scl
        self.sda = sda
        self.temp_data = 0
        self.pressure_data = 0

        time.sleep(1)
        self.i2c = I2C(self.bus, scl = self.scl, sda = self.sda, freq = 100000)
        slv = self.i2c.scan()
        #print(slv)
        for s in slv:
            buf = self.i2c.readfrom_mem(s, WHO_AM_I_REG, 1)
            #print(buf)
            if(buf[0] == CHIP_ID):
                self.slvAddr = s
                print('lps331ap found')
                #print(self.slvAddr)
                break
        time.sleep(1)

    def writeByte(self, addr, data):
        d = bytearray([data])
        self.i2c.writeto_mem(self.slvAddr, addr, d)
        
    def readByte(self, addr):
        return self.i2c.readfrom_mem(self.slvAddr, addr, 1)

    def measure(self):
        self.writeByte(RES_CONF,0x7A)  # Set sampling resolution
        self.writeByte(CTRL_REG1,0x80) # start 
        self.writeByte(CTRL_REG2,0x01) # 0x01 Set to single collection mode
        buf = self.readByte(STATUS_REG)
        if (buf[0] & 0x03) == 0x03:
            buf1 = self.readByte(PRESS_OUT_XLP)
            buf2 = self.readByte(PRESS_OUT_LP)
            buf3 = self.readByte(PRESS_OUT_H)
            buf4 = self.readByte(TEMP_OUT_L)
            buf5 = self.readByte(TEMP_OUT_H)
            P_RAW = buf1[0] + buf2[0]*256 +buf3[0]*256*256 #(int32_t)((buf3 << 16) | (buf2 << 8 | buf1); # 24bit
            T_RAW = buf4[0] + buf5[0]*256 #(int16_t)((buf5 << 8) | (buf4)) & 0xffff; # 16bit
            
            sign_bit = T_RAW & 0x8000  # 0x8000 is the symbolic bit mask of the 16-bit complement
        
            # If it is positive, return it directly
            if sign_bit == 0:
                decimal_value = T_RAW
            else:    
                # If it is negative, convert the complement to the original value
                inverted_bits = T_RAW ^ 0xFFFF  # 0xFFFF is the bitwise backmask of a 16-bit complement
                decimal_value = -(inverted_bits + 1)

            self.temp_data = decimal_value / 480 + 42.5            

            sign_bit = P_RAW & 0x800000  # 0x800000 is the symbolic bit mask of the 24-bit complement
        
            # If it is positive, return it directly
            if sign_bit == 0:
                decimal_value = P_RAW
            else:    
                # If it is negative, convert the complement to the original value
                inverted_bits = P_RAW ^ 0xFFFFFF  # 0xFFFFFF is the bit-by-bit backmask of a 24-bit complement
                decimal_value = -(inverted_bits + 1)

            self.pressure_data = decimal_value  / 4096            
    
