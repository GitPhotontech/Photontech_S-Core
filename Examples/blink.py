from machine import Pin, Timer	#Pico için pinler ve Timer kütüphaneleri dahil edildi
led = Pin(25, Pin.OUT)		#25. pin çıkış pini olarak ayarlandı
timer = Timer()			#Timer fonksiyonu timer değişkenine atandı

def blink(timer):		#Blink uygulaması için gerekli fonksiyon yazıldı
    led.toggle()		

timer.init(freq=2.5, mode=Timer.PERIODIC, callback=blink)	#timer için özel konfigürasyonlar belirlendi