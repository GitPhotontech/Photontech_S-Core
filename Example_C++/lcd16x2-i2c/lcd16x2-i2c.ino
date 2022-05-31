/*
PHOTONTECH 
  S-Core LCD örneği
  
  S-Core üzerinde ki 4. ve 5. (SDA,SCL) pine bağlı lcd yazılımda gönderilen değeri lcd ekranına yazdırıyor.
   
  Bu örnek kod C++ ile yazılarak PHOTONTECH tarafından kamuya sunulmuştur.
  
  https://github.com/GitPhotontech/Photontech_S-Core
  
*/

#include <Wire.h>  //i2c Kütüphanesi dahil edildi.
#include <LiquidCrystal_I2C.h>  //lcd kütüphanesi dahil edildi.
LiquidCrystal_I2C lcd(0x27,16,2); // LCD'nin i2c adresi ve boyutu belirtiliyor.

void setup()
{
  Wire.begin(); //i2c haberleşmesi başlatıldı.
  lcd.begin(0x27,16,2); //lcd başlatıldı

}

void loop()
{
 lcd.setCursor(0,0); // İlk satırın başlangıç noktası 
 lcd.print("Photontech"); // lcd de yazılacak yazı
 lcd.setCursor(0,1); // İkinci satırın başlangıç noktası
 lcd.print("Elektronik");// lcd de yazılacak yazı
 delay(2000);//2 saniye bekleme.
 lcd.clear();//lcd temizleniyor.
 delay(1000);//1 saniye bekleme
}