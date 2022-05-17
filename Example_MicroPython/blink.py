""" 
PHOTONTECH 

  S-Core Blink Uygulaması
  
  S-Core üzerindeki 25. pine bağlı led 1 saniye arayla yakılıp söndürülür. 
   
  Bu örnek kod PHOTONTECH tarafından kamuya sunulmuştur.
  
  https://github.com/GitPhotontech/Photontech_S-Core/tree/main/Example_MicroPython
  
"""

from machine import Pin, Timer	            #Pico için pinler ve Timer kütüphaneleri dahil edildi
led = Pin(25, Pin.OUT)		                  #25. pin çıkış pini olarak ayarlandı
timer = Timer()		                          #Timer fonksiyonu timer değişkenine atandı

def blink(timer):		                        #Blink uygulaması için gerekli fonksiyon yazıldı
    led.toggle()		        

timer.init(freq=2.5, mode=Timer.PERIODIC, callback=blink)	#timer için özel konfigürasyonlar belirlendi
