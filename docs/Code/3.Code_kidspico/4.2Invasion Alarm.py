'''
 * Filename    : Smart Safe Home: Invasion Alarm
 * Thonny      : Thonny 4.1.4
 * Auther      : http//www.keyestudio.com
'''
from machine import Pin, PWM
import time

PIR = Pin(3, Pin.IN)
led = Pin(11, Pin.OUT)
trumpet = PWM(Pin(2))

while True:
    PIR_value = PIR.value()
    if PIR_value == 1:
        trumpet.freq(880)
        trumpet.duty_u16(2000)
        led.on()
        time.sleep(0.5)
        trumpet.freq(523)
        trumpet.duty_u16(1000)
        led.off()
        time.sleep(0.5)
    else:
        trumpet.duty_u16(0)
        led.off()