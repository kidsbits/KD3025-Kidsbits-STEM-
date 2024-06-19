'''
HT16K33 1.0
'''

from machine import Pin
from machine import I2C
#import numpy as np
import time
import math

HT16K33_I2C_ADDR = 0x70    
MATRIX_LED_ON = 2
MATRIX_LED_OFF = 0

HT16K33_Oscillator_On_CMD = 0x21
HT16K33_BLINK_CMD = 0x80
HT16K33_BLINK_DISPLAYON = 0x01
HT16K33_BLINK_OFF = 0
HT16K33_BLINK_2HZ = 1
HT16K33_BLINK_1HZ = 2
HT16K33_BLINK_HALFHZ = 3
HT16K33_Brightness = 15 # 0~15
HT16K33_Brightness_CMD = 0xE0 | HT16K33_Brightness



class ht16k33:
    def __init__(self, bus, scl, sda):
        self.bus = bus
        self.scl = scl
        self.sda = sda
        self.slvAddr = 0
        self.displaybuffer = [0x0000,0x0000,0x0000,0x0000,0x0000,0x0000,0x0000,0x0000]
        self.rotation = 0
        self.i2c = I2C(self.bus, scl = self.scl, sda = self.sda, freq = 10000)
        slv = self.i2c.scan()
        print(slv)
        for s in slv:
            if(s == HT16K33_I2C_ADDR):
                self.slvAddr = s
                print('HT16K33 found')
                print(self.slvAddr)
                break
        # turn on oscillator 
        self.writeCommand(HT16K33_Oscillator_On_CMD) 
        time.sleep(0.1)
        # set blink off 
        self.writeCommand(HT16K33_BLINK_CMD | HT16K33_BLINK_DISPLAYON | (HT16K33_BLINK_OFF << 1)) 
        time.sleep(0.1)
        # set max brightness
        self.writeCommand(HT16K33_Brightness_CMD) 
        time.sleep(0.1)

    def clear(self):
        for i in range(8):
            self.displaybuffer[i] = 0

    def setRotation(self, rotate):
        rotate %= 4  # cant be higher than 3
        self.rotation = rotate
    
    def drawPixel(self, x, y, color):
        if (y < 0) or (y >= 8):
            return
        if (x < 0) or (x >= 8):
            return

        if self.rotation == 1:
            t = x
            x = y
            y = t
            x = 8 - x - 1
        elif self.rotation == 2:
            x = 8 - x - 1
            y = 8 - y - 1
        elif self.rotation == 3:
            t = x
            x = y
            y = t
            y = 8 - y - 1;
        if color: 
            self.displaybuffer[y] = self.displaybuffer[y]|(0x0001 << x)
        else:
            self.displaybuffer[y] = self.displaybuffer[y] & (~(0x0001 << x) & ~(0x0001 << (x+8)))

    def writeDisplay(self):
        # for address in range(8):    
        #     self.writeBytes(address*2, self.displaybuffer[address] >> 8, self.displaybuffer[address] & 0xFF )
        #print(self.displaybuffer)
        for address in range(16):    
            if address % 2 == 1:
                self.writeOneByte(address, self.displaybuffer[address//2] >> 8)
            else:
                self.writeOneByte(address, self.displaybuffer[address//2] & 0xFF)


    def writeCommand(self, command): # write command
        d = bytearray([command])
        self.i2c.writeto(self.slvAddr, d)

    def writeBytes(self, addr, dataL, dataH): # write data
        d = bytearray([addr, dataL, dataH])
        self.i2c.writeto(self.slvAddr, d)

    def writeOneByte(self, addr, data): # write data
        d = bytearray([data])
        self.i2c.writeto_mem(self.slvAddr, addr, d)
        
    def readByte(self, addr):
        return self.i2c.readfrom_mem(self.slvAddr, addr, 1)
 
