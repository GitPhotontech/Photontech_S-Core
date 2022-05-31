from machine import I2C
from lcd_api import LcdApi
from i2c_lcd import I2cLcd
import time

I2C_ADDR     = 0x27
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 16

i2c = I2C(0, sda=machine.Pin(0), scl=machine.Pin(1), freq=400000)
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)

while True:
    lcd.putstr("Photontech Elektronik")
    time.sleep(1)
    lcd.clear() 
    time.sleep(1)


#lcd.putstr("Hello from\n"+chr(0)+" peppe8o.com "+chr(0))