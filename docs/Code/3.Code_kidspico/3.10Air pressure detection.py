'''
 * Filename    : Air pressure detection
 * Thonny      : Thonny 4.1.4
 * Auther      : http//www.keyestudio.com
'''
from machine import Pin
import time
from LPS331AP import lps331ap

scl = Pin(5) 
sda = Pin(4)
bus = 0
pressure_temp = lps331ap(bus, scl, sda)
while True:
    pressure_temp.measure()
    print('pressure:',pressure_temp.pressure_data,'temperature:',pressure_temp.temp_data)
    time.sleep(0.1)