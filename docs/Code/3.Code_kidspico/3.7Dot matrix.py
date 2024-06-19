'''
 * Filename    : Dot matrix
 * Thonny      : Thonny 4.1.4
 * Auther      : http//www.keyestudio.com
'''
from machine import Pin
import time
from HT16K33 import ht16k33

scl = Pin(5) 
sda = Pin(4)
bus = 0

LedArray1 = [0,0,0,0,0,0,0,0,   #heart
             0,1,1,0,0,1,1,0,
             1,0,0,1,1,0,0,1,
             1,0,0,0,0,0,0,1,
             0,1,0,0,0,0,1,0,
             0,0,1,0,0,1,0,0,
             0,0,0,1,1,0,0,0,
             0,0,0,0,0,0,0,0]

Triaxial = ht16k33(bus, scl, sda)
count = 0   #rotation direction
while True:
    Triaxial.setRotation(count)
    Triaxial.clear()
    for i in range(8):
        for j in range(8):
            Triaxial.drawPixel(i, j, LedArray1[i*8+j])
    Triaxial.writeDisplay()    
    count = count + 1
    time.sleep(1)