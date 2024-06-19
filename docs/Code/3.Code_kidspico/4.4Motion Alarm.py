'''
 * Filename    : Smart Safe Home: Motion Alarm
 * Thonny      : Thonny 4.1.4
 * Auther      : http//www.keyestudio.com
'''
from machine import Pin, PWM
from AK8975C import ak8975c
import neopixel
import time

trumpet = PWM(Pin(2))  # power amplifier

scl = Pin(5) 
sda = Pin(4)
bus = 0
Triaxial = ak8975c(bus, scl, sda)

led = Pin(14, Pin.OUT)  # 6812RGB module
pixels = neopixel.NeoPixel(led, 4) 
brightness=5

while True:
    Triaxial.measure()  # measure data once
    print('x:',Triaxial.X,'y:',Triaxial.Y,'z:',Triaxial.Z)  # print the geomagnetic force on axis X Y Z
    if Triaxial.AK8975_GET_AZIMUTH(Triaxial.X, Triaxial.Y) == True:  # Print the course angle value(azimuth value) only when the angle can be calculated.
        degree = Triaxial.angle_val
        print('degree:', degree,'°')

        if degree > 0 and degree < 45:
            trumpet.duty_u16(0)
            for i in range(4):
                pixels[i] = (0,0,0)
                pixels.write()            
        else:
            for i in range(4):
                pixels[i] = (255,255,0)
                pixels.write()
            trumpet.freq(880)
            trumpet.duty_u16(2000)
            time.sleep(0.3)