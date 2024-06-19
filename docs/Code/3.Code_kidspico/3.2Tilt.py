'''
 * Filename    : Tilt
 * Thonny      : Thonny 4.1.4
 * Auther      : http//www.keyestudio.com
'''
from machine import Pin
import time

tilt = Pin(8, Pin.IN)

while True:
    tile_value = tilt.value()
    print(tile_value, end = " ")
    if  tile_value== 0:
        print("The switch is turned on")
    else:
        print("The switch is turned off")
    time.sleep(0.1)                                                                                                          