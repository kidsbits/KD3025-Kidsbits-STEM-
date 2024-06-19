'''
 * Filename    : Power amplifier
 * Thonny      : Thonny 4.1.4
 * Auther      : http//www.keyestudio.com
'''
from machine import Pin, PWM
import time

trumpet = PWM(Pin(2))

'''
-----------------------------
| Pitch names |  Frequency  |
|---------------------------|
|      C      |     523     |
|      D      |     587     |
|      E      |     659     |
|      F      |     698     |
|      G      |     784     |
|      A      |     880     |
|      B      |     988     |
-----------------------------
'''
a = [523,587,659,698,784,880,988]

while True:
    #Tone when the duty cycle is 1000
    for i in a:
        trumpet.duty_u16(1000)
        trumpet.freq(i)
        time.sleep(0.2)
    #Tone when the duty cycle is 5000
    for i in a:
        trumpet.duty_u16(5000)
        trumpet.freq(i)
        time.sleep(0.2)