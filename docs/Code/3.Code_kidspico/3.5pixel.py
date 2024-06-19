'''
 * Filename    : pixel
 * Thonny      : Thonny 4.1.4
 * Auther      : http//www.keyestudio.com
'''
#import Pin, neopiexl and time module
from machine import Pin
import neopixel
import time

#define pin
led = Pin(14, Pin.OUT)
#pixel number
pixels = neopixel.NeoPixel(led, 4) 
#brightness range: 0 - 255
brightness=5

colors=[[brightness,0,0],                    #red
        [0,brightness,0],                    #green
        [0,0,brightness],                    #blue
        [brightness,brightness,brightness],  #white
        [0,0,0]]                             #off

#nested if loop, repeatedly light up in red, green, white and goes off.
while True:
    for i in range(0,5):
        for j in range(0,4):
            pixels[j] = colors[i]  #pixel color
            pixels.write()         #write in pixels
            time.sleep_ms(50)
        time.sleep_ms(500)
    time.sleep_ms(500)