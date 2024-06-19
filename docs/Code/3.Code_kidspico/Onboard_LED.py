'''
 * Filename    : Onboard_LED
 * Thonny      : Thonny 4.1.4
 * Auther      : http//www.keyestudio.com
'''
from machine import Pin
import time

led = Pin(25, Pin.OUT)
while True:
    led.on()     
    time.sleep(1)
    led.off()    
    time.sleep(1)    