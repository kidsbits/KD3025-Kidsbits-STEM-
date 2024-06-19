'''
 * Filename    : Smart Safe Home: Card-scanning access control machine
 * Thonny      : Thonny 4.1.4
 * Auther      : http//www.keyestudio.com
'''
from machine import Pin, PWM
from mfrc522_i2c import mfrc522
import time

servo = PWM(Pin(19))
servo.freq(50)  #T = 1/f = 20ms

# IIC configuration
addr = 0x28
scl = 5
sda = 4    
rc522 = mfrc522(scl, sda, addr)
rc522.PCD_Init()  # Initialization
rc522.ShowReaderDetails()  # Display details of the PCD-MFRC522 card reader

UID =[244, 160, 150, 219] # UID code of the IC card, modify it to yours.

def angle(x):
    return int((((x + 45) * 1.8 / 270) + 0.6 )/ 20 *65535)

servo.duty_u16(angle(0))  # Initalize servo

while True:
    if rc522.PICC_IsNewCardPresent():  # Scan for a new card
        if rc522.PICC_ReadCardSerial() == True:  # New card is found
            if rc522.uid.uidByte[0 : rc522.uid.size] == UID:
                servo.duty_u16(angle(120))  # open the door
                time.sleep(3)
                servo.duty_u16(angle(0))    # close the door
            else:
                servo.duty_u16(angle(0))    # close the door
