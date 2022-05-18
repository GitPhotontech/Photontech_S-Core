/*
PHOTONTECH 
  S-Core Blink Uygulaması
  
  S-Core üzerindeki 25. pine bağlı led 1 saniye arayla yakılıp söndürülür. 
   
  Bu örnek kod C++ ile yazılarak PHOTONTECH tarafından kamuya sunulmuştur.
  
  https://github.com/GitPhotontech/Photontech_S-Core/tree/main/Example_MicroPython
  
*/

#define led 25 //led için 25 numaralı pin tanımlandı.

//void setup gerekli ayarlamaların yapıldığı bölüm.
void setup() { 
  pinMode(led, OUTPUT); //led pini çıkış olarak belirlendi.
}

//void loop programın sonsuz döngüde çalışması için oluşturulan bölüm.
void loop() {
  digitalWrite(led, HIGH);  //led HIGH konumuna çekilerek yanması sağlanıyor.
  delay(1000);              //1 saniye bekleme oluşturuluyor.
  digitalWrite(led, LOW);   //led LOW konumuna çekilerek sönmesi sağlanıyor.
  delay(1000);              //1 saniye bekleme oluşturuluyor.
}
