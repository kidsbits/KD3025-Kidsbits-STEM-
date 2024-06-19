'''
 * Filename    : Light_on
 * Thonny      : Thonny 4.1.4
 * Auther      : http//www.keyestudio.com
'''
from machine import Pin
import time

led = Pin(11, Pin.OUT)  # Set an led object and connect it to pin 11, set pin to output
while True:
    led.on()       # led on
    time.sleep(1)  # delay 1s
    led.off()      # led off
    time.sleep(1)  # delay 1s