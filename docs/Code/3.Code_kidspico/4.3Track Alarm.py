'''
 * Filename    : Smart Safe Home: Track Alarm
 * Thonny      : Thonny 4.1.4
 * Auther      : http//www.keyestudio.com
'''
from machine import Pin,ADC
import time
from HT16K33 import ht16k33

Pressure = ADC(28)  # Thin film pressure sensor

scl = Pin(5) 
sda = Pin(4)
bus = 0

LedArray1 = [0,0,0,1,1,0,0,0,   # Footprint
             1,1,0,1,1,0,1,1,
             1,1,0,0,0,0,1,1,
             0,0,0,1,1,0,0,0,
             0,0,1,1,1,1,0,0,
             0,1,1,1,1,1,1,0,
             0,1,1,1,1,1,1,0,
             0,0,1,1,1,1,0,0]

Triaxial = ht16k33(bus, scl, sda)

while True:
    Pressure_value = Pressure.read_u16()
    if Pressure_value < 40000:
        Triaxial.setRotation(0)  # Rotation direction
        Triaxial.clear()
        for i in range(8):
            for j in range(8):
                Triaxial.drawPixel(i, j, LedArray1[i*8+j])
        Triaxial.writeDisplay()    
        time.sleep(1)
    else:
        Triaxial.clear()
        Triaxial.writeDisplay() 