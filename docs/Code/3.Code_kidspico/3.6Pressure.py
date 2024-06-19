'''
 * Filename    : Pressure
 * Thonny      : Thonny 4.1.4
 * Auther      : http//www.keyestudio.com
'''
from machine import ADC  # import ADC module
import time

# configure ADC, range: 0-3.3V
# define pin io26,io27,io28,io29 to ADC channel 0,1,2,3
Pressure = ADC(28)  #Photores = ADC(2)

# read analog value every 0.1s, convert the value into voltage output
while True:
    Pressure_value = Pressure.read_u16()
    voltage = Pressure_value / 65535 * 3.3
    print('ADC Value:',Pressure_value,'   Voltage:',voltage,'V')
    time.sleep(0.1)