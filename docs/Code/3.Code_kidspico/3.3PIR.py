'''
 * Filename    : PIR
 * Thonny      : Thonny 4.1.4
 * Auther      : http//www.keyestudio.com
'''
from machine import Pin
import time

PIR = Pin(3, Pin.IN)

while True:
    PIR_value = PIR.value()
    print(PIR_value, end = " ")
    if PIR_value == 1:
        print("Some body is in this area!")
    else:
        print("No one!")
    time.sleep(0.1)