""" 
PHOTONTECH 
  S-Core 16x2 LCD örneği
  
  S-Core üzerinde ki GP0 ve GP1. pine pine bağlı lcd yazılımda gönderilen değeri lcd ekranına yazdırıyor.
   
  Bu örnek kod micropython ile yazılarak PHOTONTECH tarafından kamuya sunulmuştur.
  
  https://github.com/GitPhotontech/Photontech_S-Core
  
"""

from machine import I2C         #i2c kütüphanesi dahil edildi.
from lcd_api import LcdApi      #lcd kütüphanesi dahil edildi.
from i2c_lcd import I2cLcd      #lcd için i2c kütüphanesi dahil edildi.
import time

I2C_ADDR     = 0x27             #i2c haberleşme portu belirtildi.
I2C_NUM_ROWS = 2                #lcd satır sayısı belirtildi.
I2C_NUM_COLS = 16               #lcd sütün sayısı belirtildi.

i2c = I2C(0, sda=machine.Pin(0), scl=machine.Pin(1), freq=400000)   #i2c konfigürasyon ayarları yapıldı.
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)             #tanımlanan değerler lcd değişkenine atıldı.

while True:                                                         #sonsuz döngü oluşturuldu.
    lcd.putstr("Photontech Elektronik")                             #lcd ekranına yazı gönderildi.
    time.sleep(1)                                                   #1 saniye bekleme.
    lcd.clear()                                                     #lcd ekranı temizlendi.
    time.sleep(1)                                                   #1 saniye bekleme.

