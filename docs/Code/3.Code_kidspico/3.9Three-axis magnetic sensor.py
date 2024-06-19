'''
 * Filename    : Three-axis magnetic sensor
 * Thonny      : Thonny 4.1.4
 * Auther      : http//www.keyestudio.com
'''
from machine import Pin
from AK8975C import ak8975c
import time

scl = Pin(5) 
sda = Pin(4)
bus = 0
Triaxial = ak8975c(bus, scl, sda)

while True:
    Triaxial.measure()  # measure data once
    print('x:',Triaxial.X,'y:',Triaxial.Y,'z:',Triaxial.Z)  # print the geomagnetic force on axis X Y Z
    if Triaxial.AK8975_GET_AZIMUTH(Triaxial.X, Triaxial.Y) == True:  # Print the course angle value(azimuth value) only when the angle can be calculated.
        print('degree:', Triaxial.angle_val,'°')