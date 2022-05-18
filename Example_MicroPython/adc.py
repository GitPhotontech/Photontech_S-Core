""" 
PHOTONTECH 

  S-Core ADC örneği
  
  S-Core üzerinde ki 26. pine bağlı potansiyometre çevrildikçe okunan değer print komutu ile ekrana yazdırılıyor.

   
  Bu örnek kod micropython ile yazılarak PHOTONTECH tarafından kamuya sunulmuştur.
  
  https://github.com/GitPhotontech/Photontech_S-Core
  
"""

from machine import ADC,Pin                     #Piconun pinleri ve adc kütphanesi tanımlandı.
import time                                     #Bekleme oluşturmak için time kütüphanesi eklendi

adc = ADC(Pin(26))                              #26.pin ADC giriş pini olarak tanımlandı.

while True:                                     #Program sonsuz döngü içerisine alındı.
    print(adc.read_u16())                       #Okunan potansiyometre değerleri ekrana basılıyor.
    time.sleep(0.2)                             #0.2sn bekleme oluşturuluyor.
