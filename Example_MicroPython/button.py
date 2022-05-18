""" 
PHOTONTECH 

  S-Core Buton Örneği
  
  S-Core üzerinde ki 14. pine bağlı butona basıldığında 25.pine bağlı led yakılıyor.
  Butondan parmağımızı çektiğimizde led söndürülüyor.
   
  Bu örnek kod micropython ile yazılarak PHOTONTECH tarafından kamuya sunulmuştur.
  
  https://github.com/GitPhotontech/Photontech_S-Core
  
"""

from machine import Pin                         #Piconun pinleri tanımlandı.
import time                                     #Bekleme oluşturmak için time kütüphanesi eklendi

led = Pin(25, Pin.OUT)                          #25.Pin led için çıkış bacağı olarak tanımlandı.
button = Pin(14, Pin.IN, Pin.PULL_DOWN)         #14.Pin buton için giriş pini olarak tanımlandı.

while True:                                     #Program sonsuz döngü içerisine alındı.
    if(button.value()==True):                   #Butona basılma durumu kontrol ediliyor.
        led.value(1)                            #Butona basıldıysa led yakılıyor.
    else:
        led.value(0)                            #Butona basılmadıysa led söndürülüyor.
