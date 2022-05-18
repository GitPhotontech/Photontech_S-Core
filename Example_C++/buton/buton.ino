/*
PHOTONTECH 
  S-Core Buton Örneği
  
  S-Core üzerinde ki 14. pine bağlı butona basıldığında 25.pine bağlı led yakılıyor.
  Butondan parmağımızı çektiğimizde led söndürülüyor.
   
  Bu örnek kod C++ ile yazılarak PHOTONTECH tarafından kamuya sunulmuştur.
  
  https://github.com/GitPhotontech/Photontech_S-Core
  
*/

#define Buton 14  //14.Pin buton için tanımlandı.
#define Led 25    //25.Pin led için tanımlandı.

void setup()
{
  pinMode(Buton, INPUT); //Buton giriş olarak tanımlandı.
  pinMode(Led, OUTPUT); //Led çıkış olarak tanımlandı.
}

void loop()
{
  if(digitalRead(Buton) == 1)   //Butona basılma durumu kontrol ediliyor.
  {
      digitalWrite(Led,HIGH); //Butona basılmışsa led bacağı "HIGH" konumuna çekiliyor.
  }   
  else{
      digitalWrite(Led,LOW);  //Butona basılmamışsa led bacağı "LOW" konumuna çekiliyor.
  }
  delay(15); // Buton ark oluşması engellenmesi için 15 ms'lik bekleme oluşturuldu.
}
