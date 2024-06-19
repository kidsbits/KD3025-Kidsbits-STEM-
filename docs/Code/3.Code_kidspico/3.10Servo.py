'''
 * Filename    : Servo
 * Thonny      : Thonny 4.1.4
 * Auther      : http//www.keyestudio.com
'''
from machine import Pin, PWM
import time

servo = PWM(Pin(19))
servo.freq(50)  #T = 1/f = 20ms

def angle(x):
    return int((((x + 45) * 1.8 / 270) + 0.6 )/ 20 *65535)

while True:   
    servo.duty_u16(angle(-45))
    time.sleep(1)
    servo.duty_u16(angle(0))
    time.sleep(1)
    servo.duty_u16(angle(90))
    time.sleep(1)
    servo.duty_u16(angle(180))
    time.sleep(1)
    servo.duty_u16(angle(225))
    time.sleep(1)