'''
 * Filename    : RFID
 * Thonny      : Thonny 4.1.4
 * Auther      : http//www.keyestudio.com
'''
import machine
import time
from mfrc522_i2c import mfrc522

# IIC configuration
addr = 0x28
scl = 5
sda = 4
    
rc522 = mfrc522(scl, sda, addr)
rc522.PCD_Init()  # Initialization
rc522.ShowReaderDetails()  # Display details of the PCD-MFRC522 card reader

while True:
    if rc522.PICC_IsNewCardPresent():  # Scan for a new card
        if rc522.PICC_ReadCardSerial() == True:  # New card is found
            print("Card UID:")
            print(rc522.uid.uidByte[0 : rc522.uid.size])  # Print detailed information